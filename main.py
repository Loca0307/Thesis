from mining_restapi import *
from github_operations import *
from manual_mining_restapi import *
from semgrep_analysis import *

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

run_commit_mining_pipeline(META_DATA, META_DATA)
print("💾 🔍NOW STARTING STATS EXTRACTION")
process_all_links_files(PATHS, META_DATA, MIN_LINES,MAX_LINES, VALID_EXTENSIONS)

#print("💾 🔍NOW STARTING RANDOM COMMIT COLLECTION")
#collect_random_commits(META_DATA, OUTPUT_JSONL, CSV_OUTPUT_PATH, MIN_LINES, MAX_LINES, VALID_EXTENSIONS, max_commits=20)

'''print("🔎 NOW STARTING SEMGREP ANALYSIS")
run_semgrep_analysis_pipeline(
    AI_csv_folder="data/results",
    random_commits_csv="data/random_commits.csv",
    semgrep_results_folder="semgrep_results",
    file_extension=".py"  # Or ".c", ".java", etc., depending on your files
)
'''
