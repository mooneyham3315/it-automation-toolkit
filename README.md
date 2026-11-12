# IT Automation Toolkit

A collection of practical Python scripts built to automate repetitive IT support, log auditing, and system administration tasks.

## Scripts Included

### 1. Automated Log Parser (`log_parser.py`)
Parses raw system and application log files to isolate critical errors, service outages, and security alerts, exporting them into a structured CSV report for rapid triage.

- **Input:** Raw log files (`sample.log`)
- **Output:** Filtered summary report (`error_report.csv`)
- **Key Events Flagged:** Failed database connections, unexpected service stops, disk space warnings, and unauthorized access attempts.

#### Usage
```bash
python log_parser.py

Tech Stack
Language: Python 3 (Standard Library: csv, re)

Environment: Windows / Linux CLI
