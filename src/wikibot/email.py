import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from typing import List


def send_email(sender_email: str, sender_password: str, recipient_emails: List[str]) -> None:
    
    # Email configuration
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    
    # Generate HTML content
    html_content = """
        <html>
            <body style="font-family: Arial, sans-serif; background-color: #f9f9f9; padding: 24px;">
                <p style="color: #888; font-size: 0.9em;">Hello from wikibot!</p>
            </body>
        </html>
    """
    
    # Create message
    msg = MIMEMultipart("alternative")
    msg["Subject"] = "📚 Hello from Wikibot! 📚"
    msg["From"] = f"Wikibot <{sender_email}>"
    msg["To"] = ", ".join(recipient_emails)
    
    # Add HTML content
    html_part = MIMEText(html_content, "html")
    msg.attach(html_part)
    
    try:
        # Send email
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.send_message(msg)
        
        print(f"✅ Wikibot email sent successfully to {len(recipient_emails)} recipients")
        
    except Exception as e:
        print(f"❌ Failed to send email: {e}")
        raise