import pandas as pd
import smtplib
from email.mime.text import MIMEText
from datetime import datetime


sender_email = "dailytaskbot.psu@gmail.com"
smtp_username = "apikey"
smtp_password = ""  # paste api key here
receiver_emails = [""] # enter any email

data = pd.read_csv('data_set.csv')
data['DUE_DATE'] = pd.to_datetime(data['DUE_DATE'], format='%m/%d/%y %I:%M %p', errors='coerce')

today = datetime.today().date()
tasks_today = data[data['DUE_DATE'].dt.date == today]

if not tasks_today.empty:

    body = "Tasks Due Today:\n\n"
    for _, row in tasks_today.iterrows():
        body += f"- {row['NAME']} (Priority {row['PRIORITY']}): {row['DESCRIPTION']}\n"

    msg = MIMEText(body)
    msg['From'] = sender_email
    msg['To'] = ", ".join(receiver_emails)
    msg['Subject'] = f"Tasks Due Today - {today.strftime('%Y-%m-%d')}"

    server = smtplib.SMTP('smtp.sendgrid.net', 587)
    server.starttls()
    server.login(smtp_username, smtp_password)
    server.send_message(msg)
    server.quit()
    print("Email sent successfully!")
else:
    print("No tasks due today.")
