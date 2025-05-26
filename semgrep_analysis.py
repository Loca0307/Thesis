import os
import subprocess
import shutil

def run_semgrep_on_folder(folder_path, output_file):
    print(f"Running Semgrep on folder: {folder_path}")
    subprocess.run([
        "semgrep", "--config=auto", "--metrics=auto", folder_path,
        "--json", "--output", output_file
    ], check=True)
    print(f"Results saved to: {output_file}")

def extract_blocks_and_run_semgrep(txt_path, output_json_path, temp_snippet_folder,
                                   file_extension=".py", split_keywords=None):
    if split_keywords is None:
        split_keywords = ["FIRST COMMIT", "SECOND COMMIT", "THIRD COMMIT", "FOURTH COMMIT","FIFTH COMMIT",
                          "SIXTH COMMIT", "SEVENTH COMMIT","EIGHTH COMMIT","NINETH COMMIT","TENTH COMMIT",
                          "ELEVENTH COMMIT","TWELFTH COMMIT","THIRTEENTH COMMIT","FOURTEENTH COMMIT",
                          "FIFTEENTH COMMIT","SIXTEENTH COMMIT","SEVENTEENTH COMMIT","EIGHTEENTH COMMIT",
                          "NINETEENTH COMMIT","TWENTIETH COMMIT"]

    if not os.path.exists(txt_path) or os.path.getsize(txt_path) == 0:
        print(f"Skipping invalid or empty file: {txt_path}")
        return

    with open(txt_path, "r", encoding="utf-8") as f:
        content = f.read()

    if not content.strip():
        print(f"No content found in {txt_path}")
        return

    for keyword in split_keywords:
        content = content.replace(keyword, f"\n--- {keyword} ---\n")

    blocks = content.split("\n--- ")
    blocks = [block for block in blocks if block.strip() and not block.strip().startswith(tuple(split_keywords))]

    if not blocks:
        print(f"No valid code blocks found in {txt_path}")
        return

    # Clean snippet folder
    if os.path.exists(temp_snippet_folder):
        shutil.rmtree(temp_snippet_folder)
    os.makedirs(temp_snippet_folder, exist_ok=True)

    for i, block in enumerate(blocks):
        snippet_path = os.path.join(temp_snippet_folder, f"snippet_{i}{file_extension}")
        with open(snippet_path, "w", encoding="utf-8") as f:
            f.write(block.strip())

    run_semgrep_on_folder(temp_snippet_folder, output_json_path)

def run_semgrep_analysis_pipeline(AI_csv_folder,
                                  random_commits_csv,
                                  semgrep_results_folder,
                                  file_extension=".py"):
    os.makedirs(semgrep_results_folder, exist_ok=True)

    # Process AI commits
    ai_results_dir = os.path.join(semgrep_results_folder, "data/results")
    os.makedirs(ai_results_dir, exist_ok=True)

    for csv_file in os.listdir(AI_csv_folder):
        if not csv_file.endswith(".csv"):
            continue

        full_csv_path = os.path.join(AI_csv_folder, csv_file)
        output_file = os.path.join(ai_results_dir, f"{os.path.splitext(csv_file)[0]}_analysis.json")
        temp_folder = os.path.join(ai_results_dir, f"temp_{os.path.splitext(csv_file)[0]}")

        extract_blocks_and_run_semgrep(full_csv_path, output_file, temp_folder,
                                       file_extension=file_extension)

    # Process human commits
    random_output_file = os.path.join(semgrep_results_folder, "human_commits_analysis.json")
    random_temp_folder = os.path.join(semgrep_results_folder, "random_snippets")

    extract_blocks_and_run_semgrep(random_commits_csv, random_output_file, random_temp_folder,
                                   file_extension=file_extension)
