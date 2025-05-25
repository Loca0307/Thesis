import os
import subprocess
import pandas as pd
import pandas.errors

def run_semgrep_on_folder(folder_path, output_file):
    print(f"Running Semgrep on folder: {folder_path}")
    subprocess.run([
        "semgrep", "--config=auto", "--metrics=auto", folder_path,
        "--json", "--output", output_file
    ], check=True)
    print(f"Results saved to: {output_file}")

def run_semgrep_on_csv(csv_path, snippet_output_folder, output_file, code_column='code', file_extension=".c"):
    try:
        df = pd.read_csv(csv_path)
    except (pd.errors.EmptyDataError, FileNotFoundError) as e:
        print(f"Skipping file {csv_path}: {e}")
        return

    if df.empty:
        print(f"Skipping empty dataframe from: {csv_path}")
        return

    os.makedirs(snippet_output_folder, exist_ok=True)
    print(f"Extracting code snippets from CSV: {csv_path}")

    for i, row in df.iterrows():
        code = row.get(code_column, "")
        if not isinstance(code, str) or not code.strip():
            continue
        snippet_file = os.path.join(snippet_output_folder, f"snippet_{i}{file_extension}")
        with open(snippet_file, "w", encoding="utf-8") as f:
            f.write(code)

    print(f"Running Semgrep on extracted snippets folder: {snippet_output_folder}")
    subprocess.run([
        "semgrep", "--config=auto", "--metrics=auto", snippet_output_folder,
        "--json", "--output", output_file
    ], check=True)
    print(f"Semgrep results saved to: {output_file}")

def run_semgrep_analysis_pipeline(AI_csv_folder,
                                  random_commits_csv,
                                  semgrep_results_folder,
                                  code_column="code",
                                  file_extension=".c"):

    os.makedirs(semgrep_results_folder, exist_ok=True)

    # 1. Analyze each AI CSV file and store results in ai_commits_results
    ai_results_dir = os.path.join(semgrep_results_folder, "ai_commits_results")
    os.makedirs(ai_results_dir, exist_ok=True)

    for csv_file in os.listdir(AI_csv_folder):
        if not csv_file.endswith(".csv"):
            continue

        full_csv_path = os.path.join(AI_csv_folder, csv_file)
        if os.path.getsize(full_csv_path) == 0:
            print(f"Skipping empty file: {full_csv_path}")
            continue

        snippet_output_folder = os.path.join(ai_results_dir, f"{os.path.splitext(csv_file)[0]}_snippets")
        output_file = os.path.join(ai_results_dir, f"{os.path.splitext(csv_file)[0]}_analysis.json")
        run_semgrep_on_csv(full_csv_path, snippet_output_folder, output_file,
                           code_column=code_column, file_extension=file_extension)

    # 2. Analyze the random commits CSV
    random_snippet_folder = os.path.join(semgrep_results_folder, "random_csv_snippets")
    random_output_file = os.path.join(semgrep_results_folder, "random_commits_analysis.json")
    run_semgrep_on_csv(random_commits_csv, random_snippet_folder, random_output_file,
                       code_column=code_column, file_extension=file_extension)
