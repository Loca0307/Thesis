import subprocess
import os
import json
from typing import List
from modules import config


def prepare_nuclei_target_file(groups: List[List[dict]], target_name: str) -> str:
    """
    Each group is a list of items (each item from httpx).
    We want to choose 1 URL from each group for scanning,
    plus any items that had missing fields.
    Writes them to `nuclei_targets_{target_name}.txt`.
    Returns the path to that file.
    """
    output_file = f"nuclei_targets_{target_name}.txt"
    urls = []
    for group in groups:
        # Just pick the first item in each group
        if group and len(group) > 0:
            item = group[0]
            urls.append(item["url"])

    # Write to file
    with open(output_file, "w", encoding="utf-8") as fh:
        for url in urls:
            fh.write(url + "\n")

    return output_file


def run_nuclei(target_file: str, target_name: str) -> str:
    """
    Runs nuclei using the target_file, saves JSON results to config.NUCLEI_OUTPUT_JSON
    For clarity, let's store separate JSON for each domain to avoid collisions:
    e.g. nuclei_scan_output_{target_name}.json
    Returns path to the JSON file.
    """
    output_json = f"nuclei_scan_output_{target_name}.json"
    cmd = [
        config.NUCLEI_BIN,
        "-l",
        target_file,
        "-t",
        config.NUCLEI_TEMPLATES,
        "-c",
        "50",
        "-bs",
        "100",
        "--json-export",
        output_json,
    ]
    subprocess.run(cmd, check=True)
    return output_json


def parse_nuclei_output(json_export_file: str) -> List[dict]:
    """
    Nuclei's --json-export produces a JSON array of objects.
    Each object has keys like `info.description`, `info.severity`, and `url`.
    Returns a list of dicts with the relevant fields.
    """
    if not os.path.exists(json_export_file):
        return []

    with open(json_export_file, "r", encoding="utf-8") as fh:
        try:
            data = json.load(fh)
        except:
            data = []

    # data is a list of objects
    results = []
    for item in data:
        description = item.get("info", {}).get("description", "N/A")
        severity = item.get("info", {}).get("severity", "N/A")
        url = item.get("host", "N/A")  # or item.get("matched")
        results.append({"url": url, "description": description, "severity": severity})

    return results