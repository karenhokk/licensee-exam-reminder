import pandas as pd
import smtplib
from email.mime.text import MIMEText
from datetime import datetime

# --------------------------
# CONFIG (EDIT LOCALLY ONLY, NEVER COMMIT REAL CREDENTIALS)
# --------------------------
SMTP_SERVER = "smtp.example.com"
SMTP_PORT = 587
SENDER_EMAIL = "compliance@yourcompany.com"
SENDER_PASSWORD = "LOCAL_PASSWORD_ONLY" # DO NOT PUT REAL PASSWORD ON GITHUB
DAYS_BEFORE_DEADLINE = 14

def send_reminder_email(recipient_email, license_id, deadline):
    subject = "Reminder: Mandatory Licensee Exam Required"
    body = f"""
Dear Licensee,

This is an automated reminder.
Your license ID: {license_id}
Your exam deadline: {deadline}.
Please complete your mandatory exam before the due date.

Regards,
Compliance Team
"""
    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = SENDER_EMAIL
    msg["To"] = recipient_email

    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(SENDER_EMAIL, SENDER_PASSWORD)
            server.send_message(msg)
        print(f"Reminder sent to {recipient_email}")
        return True
    except Exception as e:
        print(f"Failed to send to {recipient_email}: {str(e)}")
        return False

def main():
    df = pd.read_csv("sample_anonymized_licensee.csv")
    df["exam_deadline"] = pd.to_datetime(df["exam_deadline"])
    today = datetime.now()

    audit_log = []

    for index, row in df.iterrows():
        if row["exam_status"] == "Completed":
            continue
        delta_days = (row["exam_deadline"] - today).days
        if 0 <= delta_days <= DAYS_BEFORE_DEADLINE:
            success = send_reminder_email(row["masked_email"], row["license_id"], row["exam_deadline"].date())
            audit_log.append({
                "license_id": row["license_id"],
                "email": row["masked_email"],
                "deadline": row["exam_deadline"].date(),
                "sent_status": success
            })
    # Save audit log locally
    audit_df = pd.DataFrame(audit_log)
    audit_df.to_csv("reminder_audit_log.csv", index=False)
    print("Audit log saved locally.")

if __name__ == "__main__":
    main()
