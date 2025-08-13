import os

from dotenv import load_dotenv

from .email import send_email


def main():
    load_dotenv()
    
    print("Hello from wikibot!")
    
    sender_email = "therandomwikibot@gmail.com"
    sender_password = os.environ.get("EMAIL_PASSWORD")
    recipient_emails = ["mattcat26@gmail.com"]
    
    category = "Musical_groups"
    
    send_email(sender_email, sender_password, recipient_emails, category)


if __name__ == "__main__":
    main()
