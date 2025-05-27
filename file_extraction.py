import os
import json

def extract_commit_id(link):
    parts = link.rstrip('/').split('/')
    return parts[-1] if parts and "commit" in parts else None

def get_extension_from_path(path):
    _, ext = os.path.splitext(path)
    return ext if ext else None

def extract_code_snippets(
    stats_file='data/stats.jsonl',
    output_dir='data/extracted_code'
):
    os.makedirs(output_dir, exist_ok=True)

    with open(stats_file, 'r', encoding='utf-8') as f:
        for line_num, line in enumerate(f, 1):
            try:
                data = json.loads(line)

                file_path = data.get("file_path", "")
                file_ext = get_extension_from_path(file_path)
                print(f"[Line {line_num}] Checking file_path: {file_path}")

                if not file_ext or not file_ext.startswith("."):
                    print(f"[Line {line_num}] Skipping: unknown or missing extension.")
                    continue

                link = data.get("Link_to_commit", "")  
                commit_id = extract_commit_id(link)
                if not commit_id:
                    print(f"[Line {line_num}] Couldn't extract commit ID from link: {link}")
                    continue

                code_lines = data.get("longest_chunk", [])
                if not code_lines:
                    print(f"[Line {line_num}] Skipping: longest_chunk is empty.")
                    continue

                if isinstance(code_lines, list):
                    code = '\n'.join(code_lines)
                else:
                    code = str(code_lines)

                filename = os.path.basename(file_path)
                final_filename = f"{commit_id}_{filename}"
                output_path = os.path.join(output_dir, final_filename)

                print(f"[Line {line_num}] Writing to {output_path}")
                with open(output_path, 'w', encoding='utf-8') as out_file:
                    out_file.write(code)

            except json.JSONDecodeError:
                print(f"[Line {line_num}] Skipping invalid JSON line.")
            except Exception as e:
                print(f"[Line {line_num}] Error processing line: {e}")
