# Licensee Exam Reminder Automation | Compliance Workflow Automation
> Python automation tool built for compliance team: auto-send email reminders to licensees for upcoming mandatory examinations.
> Background: Previously implemented similar business workflow using Microsoft Power Apps at Natixis; this Python version demonstrates alternative automation approach.

## 🛡️ Data Privacy & PII Protection (Critical Compliance Control)
This project handles licensee personal data, so privacy safeguards are built into the design:
1. **No real PII stored in GitHub repository**: The CSV committed to this repo only contains anonymized, dummy test data. Real production licensee data is stored locally only and never pushed to version control.
2. **Data anonymization**: In production workflow, direct identifiers can be masked (partial email masking, no full home address stored).
3. **.gitignore rule**: Blocks any file named `*_real_data.csv` / `production*.csv` to prevent accidental upload of confidential licensee records.
4. **Access limitation**: Production script reads sensitive files from local secured folder only; no cloud storage of raw licensee data in this solution.
5. **Retention**: Automated logs only keep audit trails for required compliance retention period, old reminder logs can be purged.
6. **Email handling**: Script only sends reminder information; no sensitive license/score details included in email body.

## Project Objective
Automatically read dynamic licensee list, filter licensees with upcoming exam deadlines, and trigger reminder emails. Replaces manual email follow-up work for compliance teams.

## Features
- Read licensee data from CSV
- Filter records by upcoming exam date
- Send bulk personalized reminder emails
- Generate simple audit log of sent reminders for compliance record keeping
- Skip sending emails to licensees marked as "completed"

## Tech Stack
Python, pandas, smtplib, CSV.
No database required; works with dynamic spreadsheet input.

## How to Run
1. Clone repository
2. Install dependencies:
```bash
pip install pandas
```
3. Use `sample_anonymized_licensee.csv` for testing.
4. Run script:
```bash
python licensee_reminder.py
```

⚠️ **IMPORTANT**: Update email credentials locally only. Do NOT save real credentials in code or push to GitHub. This repo only contains anonymized dummy data. Never upload real licensee personal data.
