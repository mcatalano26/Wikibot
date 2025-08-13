import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from typing import List


def send_email(sender_email: str, sender_password: str, recipient_emails: List[str], category: str):
    
    # Email configuration
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    
    wikipedia_endpoint = f"https://en.wikipedia.org/wiki/Special:RandomInCategory/{category}"
    
    # Generate HTML content
    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Your Random Wikipedia Article</title>
    </head>
    <body style="font-family: Arial, sans-serif; margin: 0; padding: 0; background-color: #f4f4f4;">
        
        <table role="presentation" cellspacing="0" cellpadding="0" border="0" width="100%" style="background-color: #f4f4f4;">
            <tr>
                <td align="center" style="padding: 20px;">
                    
                    <!-- Main Content Container -->
                    <table role="presentation" cellspacing="0" cellpadding="0" border="0" style="max-width: 500px; width: 100%; background-color: white; border-radius: 8px;">
                        
                        <!-- Header -->
                        <tr>
                            <td style="padding: 30px 30px 20px 30px; text-align: center; background-color: #0066cc; border-radius: 8px 8px 0 0;">
                                <h1 style="margin: 0; color: white; font-size: 24px; font-weight: normal;">📚 Wikipedia Discovery</h1>
                            </td>
                        </tr>
                        
                        <!-- Main Content -->
                        <tr>
                            <td style="padding: 30px;">
                                
                                <p style="font-size: 16px; color: #333; margin: 0 0 20px 0; line-height: 1.5;">
                                    Hello! Here's a random article from Wikipedia for you to explore:
                                </p>
                                
                                <!-- Link Button -->
                                <table role="presentation" cellspacing="0" cellpadding="0" border="0" style="margin: 25px auto;">
                                    <tr>
                                        <td style="text-align: center;">
                                            <a href="{wikipedia_endpoint}" 
                                            style="display: inline-block; background-color: #0066cc; color: white; text-decoration: none; padding: 15px 30px; border-radius: 5px; font-size: 16px; font-weight: bold; border: 2px solid #0066cc;">
                                                🎲 Read Random Article
                                            </a>
                                        </td>
                                    </tr>
                                </table>
                                
                                <p style="font-size: 14px; color: #666; margin: 20px 0 0 0; line-height: 1.4; text-align: center;">
                                    Click the button above to discover something new and interesting!
                                </p>
                                
                            </td>
                        </tr>
                        
                        <!-- Footer -->
                        <tr>
                            <td style="padding: 20px 30px; background-color: #f8f9fa; border-radius: 0 0 8px 8px; text-align: center;">
                                <p style="font-size: 12px; color: #888; margin: 0;">
                                    Powered by Wikipedia | <a href="{wikipedia_endpoint}" style="color: #0066cc; text-decoration: none;">Direct Link</a>
                                </p>
                            </td>
                        </tr>
                        
                    </table>
                    
                </td>
            </tr>
        </table>
        
    </body>
    </html>
    """
    
    # Create message
    msg = MIMEMultipart("alternative")
    msg["Subject"] = "📚 WikiBot 🧠"
    msg["From"] = f"WikiBot <{sender_email}>"
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