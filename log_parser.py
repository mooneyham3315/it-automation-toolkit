import csv
from datetime import datetime
import os
import re

# ==========================================
# CONFIGURATION (Edit these for your setup)
# ==========================================
LOG_FILE_PATH = "sample.log"
OUTPUT_CSV_PATH = "error_report.csv"

# Keywords/Severity levels to flag (Case-Insensitive)
TARGET_KEYWORDS = ["ERROR", "CRITICAL", "FAIL", "DENIED", "TIMEOUT"]


def parse_logs(file_path, keywords):
    """Reads a log file line-by-line and extracts lines matching target keywords."""
    if not os.path.exists(file_path):
        print(f"[!] Error: The file '{file_path}' was not found.")
        return []

    found_issues = []
    # Build a regex pattern like: \b(ERROR|CRITICAL|FAIL|DENIED|TIMEOUT)\b
    pattern = re.compile(
        r"\b(" + "|".join(keywords) + r")\b", re.IGNORECASE
    )

    print(f"[*] Scanning '{file_path}' for issues...")

    with open(file_path, "r", encoding="utf-8", errors="ignore") as file:
        for line_number, line in enumerate(file, start=1):
            match = pattern.search(line)
            if match:
                found_issues.append({
                    "Line_Number": line_number,
                    "Matched_Keyword": match.group(0).upper(),
                    "Log_Entry": line.strip(),
                })

    return found_issues


def export_to_csv(issues, output_path):
    """Exports the extracted log issues into a structured CSV file."""
    if not issues:
        print("[+] No errors found! System looks healthy.")
        return

    headers = ["Line_Number", "Matched_Keyword", "Log_Entry"]

    with open(output_path, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=headers)
        writer.writeheader()
        writer.writerows(issues)

    print(f"[+] Success! Found {len(issues)} issue(s).")
    print(f"[+] Report saved to: {os.path.abspath(output_path)}")


# ==========================================
# MAIN EXECUTION BLOCK
# ==========================================
if __name__ == "__main__":
    start_time = datetime.now()

    # 1. Run the parser
    detected_errors = parse_logs(LOG_FILE_PATH, TARGET_KEYWORDS)

    # 2. Print a quick preview to the VS Code terminal
    for issue in detected_errors:
        print(
            f"  -> [Line {issue['Line_Number']}] ({issue['Matched_Keyword']}): {issue['Log_Entry']}"
        )

    # 3. Export the results
    export_to_csv(detected_errors, OUTPUT_CSV_PATH)

    elapsed = datetime.now() - start_time
    print(f"[*] Task completed in {elapsed.total_seconds():.4f} seconds.")