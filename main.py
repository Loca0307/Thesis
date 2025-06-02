from mining_restapi import *
from github_operations import *
from manual_mining_restapi import *
from semgrep_analysis import *
from file_extraction import *
from extract_semgrep_stats import *

import os

# WARNING: NEVER expose your GitHub token in source code.
# It's best to load it from an environment variable.
GITHUB_TOKEN = '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' 
GITHUB_API_URL = "https://api.github.com"

if not GITHUB_TOKEN:
    raise EnvironmentError("❌ Please set the GITHUB_TOKEN environment variable!")

HEADER = {
    "Authorization": f"Bearer {GITHUB_TOKEN}",
    "Accept": "application/vnd.github.v3+json"
}

META_DATA = [GITHUB_TOKEN, GITHUB_API_URL, HEADER] 

LINKS_FOLDER = "data/links"
RESULTS_FOLDER = "data/results"
COMMITS_FOLDER = "data/commits"
N_GRAMS_FILE = "n_grams.csv"
OUTPUT_JSONL_FIRST = "data/human_1_stats.jsonl"
OUTPUT_JSONL_SECOND = "data/human_2_stats.jsonl"

PATHS = [LINKS_FOLDER, RESULTS_FOLDER, COMMITS_FOLDER, N_GRAMS_FILE] 

VALID_EXTENSIONS = {
    ".py", ".js", ".java", ".ts", ".cpp", ".go", ".php", ".cs", ".c"
}

MIN_LINES = 5
MAX_LINES = 500


# Step 1: Run AI Commit Mining Pipeline
# print("NOW STARTING AI COMMITS EXTRACTION")
# run_commit_mining_pipeline(META_DATA, PATHS)

# Step 2: Extract AI commit stats
# print("NOW STARTING STATS EXTRACTION")
# process_all_links_files(PATHS, META_DATA, MIN_LINES, MAX_LINES, VALID_EXTENSIONS)

# Step 3: Collect 20 Human Commits (first analysis)
#print("🔍 Estrazione di 20 commit random (first_analysis)...")
#collect_random_commits(META_DATA, OUTPUT_JSONL_FIRST, "data/human_commmits_results.csv", MIN_LINES, MAX_LINES, VALID_EXTENSIONS, max_commits=20)

# Step 4: Collect 200 Human Commits (second analysis) – Uncomment only if needed
print("\n🔍 Estrazione di 200 commit random (second_analysis)...")
collect_random_commits(
    META_DATA,
    OUTPUT_JSONL_SECOND,
    MIN_LINES,
    MAX_LINES,
    VALID_EXTENSIONS,
    200
)

# Step 5: Extract code from stats
# print("NOW STARTING EXTRACTING ALL CODE FILES FROM STATS.JSONL")
# extract_code_snippets('data/stats.jsonl', 'data/extracted_code/AI_files')
# extract_code_snippets(OUTPUT_JSONL_FIRST, 'data/extracted_code/human_files')

# Step 6: Run Semgrep analysis
# print("NOW STARTING SEMGREP ANALYSIS")
# run_multilang_semgrep_analysis("data/extracted_code/AI_files", "semgrep_results/AI_code", "AI_commits_analysis.json")
# run_multilang_semgrep_analysis("data/extracted_code/human_files", "semgrep_results/human_code", "human_commits_analysis.json")

# Step 7: Extract summary statistics
# print("NOW STARTING EXTRACTING SEMGREP STATISTICS")
# extract_semgrep_summary("semgrep_results/all_semgrep_results.json", "semgrep_results/semgrep_stats.csv")

print("✅ Pipeline completata.")
