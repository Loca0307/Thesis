import os
import json
import csv
from collections import Counter

def extract_semgrep_summary(json_file_path, output_csv_path):
    # Initialize counters
    severity_counter = Counter()
    cwe_counter = Counter()
    tech_counter = Counter()
    vuln_class_counter = Counter()
    
    # Read the JSON file
    with open(json_file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    results = data.get("results", [])
    print(f"Processing {len(results)} Semgrep findings...")

    for entry in results:
        extra = entry.get("extra", {})
        metadata = extra.get("metadata", {})

        # Severity
        severity = extra.get("severity", "UNKNOWN")
        severity_counter[severity] += 1

        # CWE - can be list or string
        cwes = metadata.get("cwe", [])
        if isinstance(cwes, list):
            cwe_counter.update(cwes)
        elif isinstance(cwes, str):
            cwe_counter[cwes] += 1

        # Technology
        techs = metadata.get("technology", [])
        if isinstance(techs, list):
            tech_counter.update(techs)
        elif isinstance(techs, str):
            tech_counter[techs] += 1

        # Vulnerability Class
        vuln_classes = metadata.get("vulnerability_class", [])
        if isinstance(vuln_classes, list):
            vuln_class_counter.update(vuln_classes)
        elif isinstance(vuln_classes, str):
            vuln_class_counter[vuln_classes] += 1

    # Write summary CSV
    with open(output_csv_path, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Metric", "Item", "Count"])

        for sev, count in severity_counter.items():
            writer.writerow(["Severity", sev, count])

        for cwe, count in cwe_counter.items():
            writer.writerow(["CWE", cwe, count])

        for tech, count in tech_counter.items():
            writer.writerow(["Technology", tech, count])

        for vc, count in vuln_class_counter.items():
            writer.writerow(["Vulnerability Class", vc, count])

    print(f"✅ Summary written to {output_csv_path}")
