from mining_restapi import *
from github_operations import *
from manual_mining_restapi import *

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

PATHS = [LINKS_FOLDER, RESULTS_FOLDER, COMMITS_FOLDER, N_GRAMS_FILE] 

VALID_EXTENSIONS = {
    ".py", ".js", ".java", ".ts", ".cpp", ".go", ".php", ".cs", ".c"
}

MIN_LINES = 5
MAX_LINES = 500

#run_commit_mining_pipeline(META_DATA, META_DATA)
#print("💾 🔍NOW STARTING STATS EXTRACTION")
#process_all_links_files(PATHS, META_DATA, MIN_LINES,MAX_LINES, VALID_EXTENSIONS)

print("💾 🔍NOW STARTING RANDOM COMMIT COLLECTION")
OUTPUT_JSONL = os.path.join("data/" "random_commits.jsonl")
collect_random_commits(META_DATA, OUTPUT_JSONL, MIN_LINES, MAX_LINES, VALID_EXTENSIONS, max_commits=20)
