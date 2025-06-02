import aiosmtpd
from aiosmtpd.handlers import Message
from email.parser import Parser

class EmailHandler(Message):
    def __init__(self):
        super().__init__()

    async def handle_DATA(self, server, session, envelope):
        # Parse the email message content
        message = Parser().parsestr(envelope.content.decode())
        subject = message.get("Subject", "No Subject")
        sender = message.get("From", "Unknown Sender")
        recipient = message.get("To", "Unknown Recipient")
        body = envelope.content.decode()

        # Create or append to a .txt file
        with open("emails_received.txt", "a") as file:
            file.write(f"--- New Email ---\n")
            file.write(f"From: {sender}\n")
            file.write(f"To: {recipient}\n")
            file.write(f"Subject: {subject}\n")
            file.write(f"Body:\n{body}\n")
            file.write("-" * 40 + "\n")

        print(f"✅ Email saved to emails_received.txt")
        return "250 Message accepted for delivery"

# Set up the SMTP server
async def run_server():
    handler = EmailHandler()
    server = aiosmtpd.controller.Controller(handler, hostname='localhost', port=1025)
    server.start()
    print("🚀 Local SMTP server running on localhost:1025")

if __name__ == "__main__":
    import asyncio
    asyncio.run(run_server())