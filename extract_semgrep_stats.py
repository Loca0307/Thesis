import os
import json
import csv
from collections import Counter, defaultdict
from statistics import median, mean

def extract_semgrep_summary(json_file_path, output_csv_path):
    severity_counter = Counter()
    cwe_counter = Counter()
    tech_counter = Counter()
    vuln_class_counter = Counter()
    file_finding_counts = defaultdict(int)
    file_vuln_positions = defaultdict(list)

    with open(json_file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    results = data.get("results", [])
    print(f"Processing {len(results)} Semgrep findings...")

    for entry in results:
        extra = entry.get("extra", {})
        metadata = extra.get("metadata", {})
        path = entry.get("path", "UNKNOWN_FILE")
        file_finding_counts[path] += 1

        start = entry.get("start", {}).get("line")
        end = entry.get("end", {}).get("line")
        if start is not None and end is not None:
            file_vuln_positions[path].append((start, end))

        severity = extra.get("severity", "UNKNOWN")
        severity_counter[severity] += 1

        cwes = metadata.get("cwe", [])
        if isinstance(cwes, list):
            cwe_counter.update(cwes)
        elif isinstance(cwes, str):
            cwe_counter[cwes] += 1

        techs = metadata.get("technology", [])
        if isinstance(techs, list):
            tech_counter.update(techs)
        elif isinstance(techs, str):
            tech_counter[techs] += 1

        vuln_classes = metadata.get("vulnerability_class", [])
        if isinstance(vuln_classes, list):
            vuln_class_counter.update(vuln_classes)
        elif isinstance(vuln_classes, str):
            vuln_class_counter[vuln_classes] += 1

    counts = list(file_finding_counts.values())
    min_findings = min(counts) if counts else 0
    max_findings = max(counts) if counts else 0
    median_findings = median(counts) if counts else 0
    avg_findings = mean(counts) if counts else 0

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

        writer.writerow(["---", "---", "---"])
        writer.writerow(["Finding Stats", "Minimum", min_findings])
        writer.writerow(["Finding Stats", "Maximum", max_findings])
        writer.writerow(["Finding Stats", "Median", median_findings])
        writer.writerow(["Finding Stats", "Average", round(avg_findings, 2)])

        writer.writerow(["---", "---", "---"])
        writer.writerow(["File-level Finding Summary", "Filename", "Finding Count & Positions"])
        for file, count in file_finding_counts.items():
            positions = file_vuln_positions.get(file, [])
            pos_str = "; ".join([f"(start: {s}, end: {e})" for s, e in positions])
            writer.writerow(["File", file, f"{count} findings at {pos_str}"])

    print(f"✅ Summary with file positions written to {output_csv_path}")
