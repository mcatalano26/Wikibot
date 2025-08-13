import json
import os
import random
from urllib.request import urlopen

import requests  # type: ignore
from dotenv import load_dotenv

from .email import send_email


def main():
    load_dotenv()
    
    print("Hello from wikibot!")
    
    request = {"action": "query", "list": "categorymembers", "cmtitle": "Category:Philosophy", "cmlimit": "500"}
    last_continue = {}
    # the below was from wikipedia's own documentation, but does not work as expected
    while False:
        req = request.copy()
        req.update(last_continue)
        result = requests.get("https://en.wikipedia.org/w/api.php", params=req).json()
        if 'error' in result:
            raise Exception(result['error'])
        if 'warnings' in result:
            print(result['warnings'])
        if 'query' in result:
            print(result['query'])
        if 'continue' not in result:
            break
        last_continue = result['continue']
        
    pages = urlopen("https://en.wikipedia.org/w/api.php?action=query&list=categorymembers&cmtitle=Category:Class-based%20programming%20languages&format=json&cmlimit=500")
    data = json.load(pages)
    query = data['query']
    category = query['categorymembers']
    for x in category:
        print(x['title'])
    
    sender_email = "therandomwikibot@gmail.com"
    sender_password = os.environ.get("EMAIL_PASSWORD")
    recipient_emails = ["mattcat26@gmail.com"]
    
    categories = ["Musical groups", "Philosophy", "Culture"]
    
    category = random.choice(categories)

    wikipedia_endpoint = f"https://en.wikipedia.org/wiki/Special:RandomInCategory/{category}"
    
    exit(0)
    
    send_email(sender_email, sender_password, recipient_emails, wikipedia_endpoint)


if __name__ == "__main__":
    main()
