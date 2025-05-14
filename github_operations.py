import os
import csv
import json
import requests
import time

def get_commit_diff(commit_url, headers, retries=3, delay=2):
    full_url = commit_url + ".diff"

    for attempt in range(retries):
        time.sleep(delay)  
        response = requests.get(full_url, headers={**headers, "Accept": "application/vnd.github.v3.diff"})

        if response.status_code == 200:
            return response.text
        elif response.status_code == 406:
            print(f"❌ 406 Not Acceptable for diff — falling back to JSON for: {commit_url}")
            response = requests.get(commit_url, headers={**headers, "Accept": "application/vnd.github.v3+json"})
            if response.status_code == 200:
                data = response.json()
                patch_texts = [file.get("patch") for file in data.get("files", []) if file.get("patch")]
                return "\n".join(patch_texts)
        elif response.status_code == 404:
            print(f"❌ 404 Not Found — Possibly private or deleted commit: {commit_url}")
            break
        elif response.status_code == 429:
            print(f"❌ 429 Too Many Requests — rate limited on attempt {attempt+1}/{retries} for {commit_url}")
            time.sleep(delay * (attempt + 1))
        elif response.status_code >= 500:
            print(f"❌ Server error {response.status_code} — attempt {attempt+1}/{retries} for {commit_url}")
            time.sleep(delay)
        else:
            print(f"❌ Error fetching commit diff ({full_url}): {response.status_code}")
            break

    return None


def extract_largest_added_chunk(diff, min_lines, valid_extensions):
    largest_chunk = []
    current_chunk = []
    current_file = None
    file_with_largest_chunk = None

    def is_valid_extension(filename):
        extension = os.path.splitext(filename.lower())[1]
        return extension in valid_extensions

    for line in diff.split('\n'):
        if line.startswith("diff --git"):
            parts = line.split(" b/")
            if len(parts) == 2:
                current_file = parts[1].strip()
        elif line.startswith('+++') or line.startswith('---'):
            continue
        elif line.startswith('+') and not line.startswith('+++'):
            current_chunk.append(line[1:])
        else:
            if len(current_chunk) > len(largest_chunk) and current_file and is_valid_extension(current_file):
                largest_chunk = current_chunk
                file_with_largest_chunk = current_file
            current_chunk = []

    if len(current_chunk) > len(largest_chunk) and current_file and is_valid_extension(current_file):
        largest_chunk = current_chunk
        file_with_largest_chunk = current_file

    if len(largest_chunk) < min_lines:
        return [], 0, None
    return largest_chunk, len(largest_chunk), file_with_largest_chunk

def count_files_impacted(diff):
    return sum(1 for line in diff.splitlines() if line.startswith('diff --git'))

def process_links_file(link_file_path, result_file_path, min_lines, max_lines, jsonl_writer, valid_extensions, headers):
    with open(link_file_path, mode='r') as infile:
        reader = csv.reader(infile)
        rows = [row for row in reader if len(row) >= 2]

    with open(result_file_path, mode='w', newline='') as result_out:
        result_writer = csv.writer(result_out)

        for link_number, row in enumerate(rows, start=1):
            ngram_token, commit_url = row[0], row[1]

            result_writer.writerow([])
            result_writer.writerow([f"LINK NUMBER {link_number}"])

            diff_text = get_commit_diff(commit_url, headers)

            if diff_text:
                longest_chunk, chunk_length, file_path = extract_largest_added_chunk(diff_text, min_lines, valid_extensions)
                files_impacted = count_files_impacted(diff_text)

                if chunk_length == 0:
                    result_writer.writerow(["Not enough lines"])
                    continue
                elif chunk_length > max_lines:
                    result_writer.writerow(["Too many lines"])
                    continue
                else:
                    result_writer.writerow([])
                    result_writer.writerow([f"File path: {file_path}"])
                    result_writer.writerow(["\n".join(longest_chunk)])

                    json_data = {
                        "Link_to_commit": commit_url,
                        "n-gram matched": ngram_token,
                        "n_lines_longer_change": chunk_length,
                        "n_files_impacted": files_impacted,
                        "longest_chunk": longest_chunk,
                        "file_path": file_path
                    }
                    jsonl_writer.write(json.dumps(json_data) + "\n")
            else:
                result_writer.writerow(["Error fetching diff"])

def process_all_links_files(paths, headers, min_lines, max_lines, valid_extensions):
    os.makedirs(paths[1], exist_ok=True)  

    STATS_JSONL_PATH = os.path.join("data", "stats.jsonl")

    with open(STATS_JSONL_PATH, mode='w', encoding='utf-8') as jsonl_writer:
        for filename in os.listdir(paths[0]):
            if filename.startswith("link") and filename.endswith(".csv"):
                index = filename.replace("link", "").replace(".csv", "")
                link_file = os.path.join(paths[0], filename)
                result_file = os.path.join(paths[1], f"results{index}.csv")

                print(f"📁 Processing {filename} ➞ {os.path.basename(result_file)}")
                process_links_file(link_file, result_file, min_lines, max_lines, jsonl_writer, valid_extensions, headers)
                print(f"✅ Done: saved results to {result_file} and appended stats to JSONL\n")
