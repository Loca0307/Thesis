import os
import shutil
import subprocess
import json

def run_multilang_semgrep_analysis(input_folder,
                                    output_folder,
                                    merged_output_filename):
    os.makedirs(output_folder, exist_ok=True)
    temp_parent_folder = "temp_lang_folders"
    os.makedirs(temp_parent_folder, exist_ok=True)

    extensions = {
        "py": ".py",
        "js": ".js",
        "java": ".java",
        "ts": ".ts",
        "cpp": ".cpp",
        "go": ".go",
        "php": ".php",
        "cs": ".cs",
        "c": ".c"
    }

    merged_results = {"results": []}

    for lang, ext in extensions.items():
        temp_lang_folder = os.path.join(temp_parent_folder, lang)
        os.makedirs(temp_lang_folder, exist_ok=True)

        for root, _, files in os.walk(input_folder):
            for file in files:
                if file.endswith(ext):
                    full_path = os.path.join(root, file)
                    rel_path = os.path.relpath(full_path, input_folder)
                    dest_path = os.path.join(temp_lang_folder, rel_path)
                    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
                    shutil.copy2(full_path, dest_path)

        if not any(os.scandir(temp_lang_folder)):
            print(f"⚠️ No files with extension {ext} found, skipping {lang}.")
            shutil.rmtree(temp_lang_folder)
            continue

        output_file = os.path.join(output_folder, f"{lang}_semgrep_results.json")
        print(f"🔍 Running Semgrep for *.{ext} files...")
        subprocess.run([
            "semgrep", "--config=auto", "--metrics=auto", temp_lang_folder,
            "--json", "--output", output_file
        ], check=True)
        print(f"✅ Semgrep output for {lang} saved to {output_file}")

        with open(output_file, 'r', encoding='utf-8') as f:
            lang_results = json.load(f)
            merged_results["results"].extend(lang_results.get("results", []))

        shutil.rmtree(temp_lang_folder)

    # Clean up parent temp folder
    if os.path.exists(temp_parent_folder):
        shutil.rmtree(temp_parent_folder)

    merged_output_path = os.path.join(output_folder, merged_output_filename)
    with open(merged_output_path, 'w', encoding='utf-8') as f:
        json.dump(merged_results, f, indent=2)

    print(f"\n🎉 All results merged and saved to: {merged_output_path}")
