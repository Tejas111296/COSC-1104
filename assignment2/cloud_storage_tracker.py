"""
Cloud Storage Usage Tracker
Author: Tejas Tondase
Date: 15 November 2024
Description: This script monitors folder sizes to track cloud storage usage 
             and alerts users when usage nears the set limit.
"""

import os
import smtplib
from email.mime.text import MIMEText

def calculate_folder_size(folder_path):
    """Calculate the total size of a folder in bytes with error handling."""
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(folder_path):
        for file in filenames:
            file_path = os.path.join(dirpath, file)
            try:
                total_size += os.path.getsize(file_path)
            except Exception as e:
                print(f"Error accessing {file_path}: {e}")
    return total_size


def send_email_alert(current_size, limit, recipient_email):
    """Send an email alert when storage usage exceeds a certain limit."""
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    sender_email = "your_email@example.com"
    sender_password = "your_password"
    
    subject = "Cloud Storage Alert: Usage Exceeded Limit"
    body = f"Your current usage is {current_size / 1e6:.2f} MB, exceeding the limit of {limit / 1e6:.2f} MB."
    message = MIMEText(body)
    message["Subject"] = subject
    message["From"] = sender_email
    message["To"] = recipient_email

    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.send_message(message)
        print("Email alert sent!")
    except Exception as e:
        print(f"Failed to send email: {e}")

def main():
    folder_path = input("Enter the path to the folder: ")
    storage_limit = float(input("Enter the storage limit in MB: ")) * 1e6
    recipient_email = input("Enter your email address for alerts: ")
    
    current_size = calculate_folder_size(folder_path)
    print(f"Current folder size: {current_size / 1e6:.2f} MB")
    
    if current_size > storage_limit:
        print("Warning: Storage usage exceeds the limit!")
        send_email_alert(current_size, storage_limit, recipient_email)
    else:
        print("Storage usage is within the limit.")

if __name__ == "__main__":
    main()