import os
import requests
import csv
import time


def get_rate_limit(headers):
    """Controlla il rate limit delle API di GitHub."""
    url = f"{headers[1]}/rate_limit"
    response = requests.get(url, headers=headers[2]).json()
    remaining = response["rate"]["remaining"]
    reset_time = response["rate"]["reset"]
    return remaining, reset_time

def wait_if_rate_limited(headers):
    """Attende se il rate limit è stato superato."""
    remaining, reset_time = get_rate_limit(headers)
    if remaining == 0:
        wait_time = reset_time - time.time()
        print(f"⚠️ Rate limit superato. Attendo {int(wait_time)} secondi...")
        time.sleep(wait_time)

def fetch_and_save_results(headers, url, filename, process_function, fields):
    """Scarica i risultati gestendo la paginazione e salva progressivamente."""
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fields)   
        writer.writeheader()
        
        while url:
            wait_if_rate_limited(headers)
            response = requests.get(url, headers=headers[2])
            if response.status_code != 200:
                print(f"❌ Errore nella richiesta: {response.json()}")
                break
            
            data = response.json()
            processed_data = process_function(data.get("items", []))
            writer.writerows(processed_data)
            print(f"💾 Salvati {len(processed_data)} risultati parziali in {filename}")
            
            url = response.links["next"]["url"] if "next" in response.links else None

def search_commits(headers, query):
    """Cerca in tutti i commit."""
    url = f"{headers[1]}/search/commits?q={query}&per_page=100"
    return url
   

def search_pull_requests(headers, query):
    """Cerca in tutte le pull request."""
    url = f"{headers[1]}/search/issues?q={query}+type:pr&per_page=100"
    return url

def process_commits(data, ngram):
    """Estrae e formatta i dati dei commit per il salvataggio in CSV, solo se il messaggio contiene l'ngram esatto."""
    results = []
    for item in data:
        message = item["commit"]["message"]
        if ngram is None or ngram.lower() in message.lower():
            results.append({
                "message": message,
                "author": item["commit"]["author"]["name"],
                "date": item["commit"]["author"]["date"],
                "url": item["html_url"]
            })
    return results


def extract_github_links(input_csv_path, output_csv_path, ngram):
    """Estrae i link GitHub da un CSV di commit e li salva in un nuovo file, insieme al n-gram."""
    with open(input_csv_path, mode='r', newline='', encoding='utf-8') as infile:
        reader = csv.DictReader(infile)
        
        with open(output_csv_path, mode='w', newline='', encoding='utf-8') as outfile:
            writer = csv.writer(outfile)

            for row in reader:
                url = row.get("url", "")
                if url.startswith("https://github.com/"):
                    writer.writerow([ngram, url])   

def process_pull_requests(data):
    """Estrae e formatta i dati delle pull request per il salvataggio in CSV."""
    return [{
        "title": item["title"],
        "user": item["user"]["login"],
        "created_at": item["created_at"],
        "url": item["html_url"]
    } for item in data]


def read_tokens_from_csv(filename):
    """Legge ogni riga di un file CSV e aggiunge ogni riga all'array."""
    tokens = []
    with open(filename, mode='r', newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if row:  
                tokens.append(row[0].strip())  
    return tokens


def run_commit_mining_pipeline(headers, paths):
    tokens = read_tokens_from_csv(paths[3]) 
    
    os.makedirs(paths[2], exist_ok=True)
    os.makedirs(paths[0], exist_ok=True)

    for i, token_to_search in enumerate(tokens):
        print(f"🔍 Cercando commit per token {i + 1}: '{token_to_search}'...")
        commits_url = search_commits(headers, token_to_search)

        commit_filename = os.path.join(paths[2], f"commit__{i + 1}.csv")
        fetch_and_save_results(
            headers, 
            commits_url, 
            commit_filename, 
            lambda data: process_commits(data, ngram=token_to_search), 
            ["message", "author", "date", "url"]
        )
        print(f"📄 Risultati salvati in {commit_filename}")

        link_filename = os.path.join(paths[0], f"link{i + 1}.csv")
        extract_github_links(commit_filename, link_filename, token_to_search)
        print(f"🔗 Link GitHub salvati in {link_filename}")

    print(f"✅ Tutti i risultati sono stati salvati.")
