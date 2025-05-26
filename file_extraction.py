import os
import json
from urllib.parse import urlparse

def extract_commit_id(link):
    """Extract commit ID from a GitHub commit URL."""
    parts = link.rstrip('/').split('/')
    return parts[-1] if parts and "commit" in parts else None

def run_python_commit_extraction_pipeline(stats_file, output_dir):
    """Extracts Python files from a stats JSONL file and writes them to output_dir."""
    os.makedirs(output_dir, exist_ok=True)
    print(f"Processing stats file: {stats_file}")

    with open(stats_file, 'r', encoding='utf-8') as f:
        for line_num, line in enumerate(f, 1):
            try:
                data = json.loads(line)

                file_path = data.get("file_path", "")
                if not file_path.endswith(".py"):
                    continue  # Skip non-Python files

                link = data.get("Link_to_commit", "")  # Match actual JSON key
                commit_id = extract_commit_id(link)
                if not commit_id:
                    continue  # Skip if commit ID can't be extracted

                code_lines = data.get("longest_chunk", [])
                if not code_lines:
                    continue

                code = '\n'.join(code_lines) if isinstance(code_lines, list) else str(code_lines)

                filename = os.path.basename(file_path)
                final_filename = f"{commit_id}_{filename}"
                output_path = os.path.join(output_dir, final_filename)

                with open(output_path, 'w', encoding='utf-8') as out_file:
                    out_file.write(code)

            except json.JSONDecodeError:
                print(f"[Line {line_num}] Skipping invalid JSON line.")
            except Exception as e:
                print(f"[Line {line_num}] Error processing line: {e}")
