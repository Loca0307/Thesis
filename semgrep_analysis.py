import os
import subprocess

def run_python_commit_semgrep_analysis(input_folder="data/python_commits",
                                       output_folder="semgrep_results",
                                       output_filename="python_commits_analysis.json"):
    """Run Semgrep analysis on Python commits in a folder and save the result to a JSON file."""
    os.makedirs(output_folder, exist_ok=True)
    output_file = os.path.join(output_folder, output_filename)

    print(f"Running Semgrep on folder: {input_folder}")
    subprocess.run([
        "semgrep", "--config=auto", "--metrics=auto", input_folder,
        "--json", "--output", output_file
    ], check=True)
    print(f"Results saved to: {output_file}")
