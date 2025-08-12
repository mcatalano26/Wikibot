
import os

from dotenv import load_dotenv

from .email import send_email


def main():
    os.environ["EMAIL_PASSWORD"] = "Nothing"
    print('original pass')
    print(os.getenv("EMAIL_PASSWORD"))
    
    result= load_dotenv("/Users/mattcatalano/repos/Wikibot/.env")
    print(f"load_dotenv() returned: {result}")
    
    sender_email = "mattcat26@gmail.com"

    sender_password = os.getenv("EMAIL_PASSWORD")
    print('[assw]')
    print(sender_password)
    exit(0)
    recipient_emails = ["mattcat26@gmail.com"]
    send_email(sender_email, sender_password, recipient_emails)


if __name__ == "__main__":
    main()
