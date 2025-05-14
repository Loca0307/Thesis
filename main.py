from mining_restapi import *
from github_operations import *


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

PATHS = [LINKS_FOLDER, RESULTS_FOLDER, COMMITS_FOLDER, N_GRAMS_FILE] 

VALID_EXTENSIONS = {
    ".py", ".js", ".java", ".ts", ".cpp", ".go", ".php", ".cs", ".c"
}

MIN_LINES = 5
MAX_LINES = 500

#run_commit_mining_pipeline(headers, paths)
print("💾 🔍NOW STARTING STATS EXTRACTION")
process_all_links_files(PATHS, META_DATA, MIN_LINES,MAX_LINES, VALID_EXTENSIONS)
