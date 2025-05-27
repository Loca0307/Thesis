from mining_restapi import *
from github_operations import *
from manual_mining_restapi import *
from semgrep_analysis import *
from file_extraction import *
from extract_semgrep_stats import *

GITHUB_TOKEN = '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'
GITHUB_API_URL = "https://api.github.com"

HEADER = {
    "Authorization": f"Bearer {GITHUB_TOKEN}",
    "Accept": "application/vnd.github.v3+json"
}

META_DATA = [GITHUB_TOKEN, GITHUB_API_URL, HEADER] 

LINKS_FOLDER = "data/links"
RESULTS_FOLDER = "data/results"
COMMITS_FOLDER = "data/commits"
N_GRAMS_FILE = "n_grams.csv"
OUTPUT_JSONL = "data/random_commits.jsonl"

PATHS = [LINKS_FOLDER, RESULTS_FOLDER, COMMITS_FOLDER, N_GRAMS_FILE] 

VALID_EXTENSIONS = {
    ".py", ".js", ".java", ".ts", ".cpp", ".go", ".php", ".cs", ".c"
}

MIN_LINES = 5
MAX_LINES = 500

#run_commit_mining_pipeline(META_DATA, PATHS)
#print("💾 🔍NOW STARTING STATS EXTRACTION")
#process_all_links_files(PATHS, META_DATA, MIN_LINES,MAX_LINES, VALID_EXTENSIONS)

#print("💾 🔍NOW STARTING RANDOM COMMIT COLLECTION")
#collect_random_commits(META_DATA, OUTPUT_JSONL, CSV_OUTPUT_PATH, MIN_LINES, MAX_LINES, VALID_EXTENSIONS, max_commits=20)

#print (NOW STARTING EXTRACTING PYTHON FILES)
#run_python_commit_extraction_pipeline("data/stats.jsonl", "data/python_commits")

#print("💾 🔍NOW STARTING SEMGREP ANALYSIS")
#run_python_commit_semgrep_analysis("data/python_commits", "semgrep_results", "python_commits_analysis.json")

#print(NOW STARTING EXTRACTING SEMGREP STATISTICS)
extract_semgrep_summary("semgrep_results/python_commits_analysis.json", "semgrep_results/semgrep_stats.csv")