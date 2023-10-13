# Create class EmailSender App
class EmailSenderApp():
    def __init__(self):
        super().__init__()

    # Define meethod to send single email
    def send_single_email(self):
        sender_email = input("Enter Sender Email\n")
        sender_password = input("Enter Sender Password\n")
        recipient_email = input("Enter Recipient Email\n")
        subject = input("Enter Email Subject\n")
        message_body = input("Enter Message\n")

        print("Sender Email: ",sender_email)
        print("Sender Password: ",sender_password)
        print("Recipient Email: ",recipient_email)
        print("Subject: ",subject)
        print("Message Body: ",message_body)

        
        

# Define function main and call class EmailSenderApp()
def main():
    app = EmailSenderApp()
    app.send_single_email()

# Call main() function
if __name__ == "__main__":
    main()

