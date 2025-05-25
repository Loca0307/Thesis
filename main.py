from mining_restapi import *
from github_operations import *
from manual_mining_restapi import *
from semgrep_analysis import run_semgrep_analysis_pipeline  # assuming you saved the semgrep code in semgrep_analysis.py

GITHUB_TOKEN = '.'
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

#run_commit_mining_pipeline(META_DATA, META_DATA)
#print("💾 🔍NOW STARTING STATS EXTRACTION")
#process_all_links_files(PATHS, META_DATA, MIN_LINES,MAX_LINES, VALID_EXTENSIONS)

#print("💾 🔍NOW STARTING RANDOM COMMIT COLLECTION")
#collect_random_commits(META_DATA, OUTPUT_JSONL, CSV_OUTPUT_PATH, MIN_LINES, MAX_LINES, VALID_EXTENSIONS, max_commits=20)

print("🔎 NOW STARTING SEMGREP ANALYSIS")
run_semgrep_analysis_pipeline(
    RESULTS_FOLDER,
    "data/random_commmits_results.csv",
    "data/semgrep_results",  
    code_column="code",
    file_extension=".c"
)
