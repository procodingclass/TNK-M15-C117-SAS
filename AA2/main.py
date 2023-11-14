import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class EmailSenderApp():
    def __init__(self):
        super().__init__()

    def send_single_email(self):
        sender_email = input("Enter Sender Email\n")
        sender_password = input("Enter Sender Password\n")
        recipients_email = input(
            "Enter Comma Seprated Recipient Email\n").strip()
        subject = input("Enter Email Subject\n")
        message_body = input("Enter Message\n")
        recipients_email = recipients_email.split(",")

        for email_id in recipients_email:
            try:
                # Fix the host and port number to setup SMTP server
                smtp_server = smtplib.SMTP("smtp.gmail.com", 587)
                # Start the TLS service
                smtp_server.starttls()
                # Login with creadentials
                smtp_server.login(sender_email, sender_password)

                message = MIMEMultipart()
                message["From"] = sender_email
                message["To"] = email_id
                message["Subject"] = subject
                message.attach(MIMEText(message_body, "plain"))

                smtp_server.sendmail(
                    sender_email, email_id, message.as_string())
                smtp_server.quit()
                print("Email Sent", "Email sent successfully!")

            except Exception as e:
                print("Error", f"An error occurred: {str(e)}")


def main():
    app = EmailSenderApp()
    app.send_single_email()


if __name__ == "__main__":
    main()
