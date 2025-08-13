import os

from dotenv import load_dotenv


def main():
    load_dotenv()
    print(os.environ.get("EMAIL_PASSWORD"))
    
    print("Hello from wikibot!")


if __name__ == "__main__":
    main()
