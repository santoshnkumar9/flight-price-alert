import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from config import EMAIL_SENDER, EMAIL_PASSWORD, TWILIO_SID, TWILIO_AUTH_TOKEN, TWILIO_PHONE
from twilio.rest import Client

def send_notification(message, email_to, whatsapp_to):
    send_email_notification(message, email_to)
    send_whatsapp_notification(message, whatsapp_to)

def send_email_notification(message, recipient):
    try:
        msg = MIMEMultipart()
        msg['From'] = EMAIL_SENDER
        msg['To'] = recipient
        msg['Subject'] = "✈️ Flight Price Alert"

        msg.attach(MIMEText(message, 'plain'))

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(EMAIL_SENDER, EMAIL_PASSWORD)
        server.send_message(msg)
        server.quit()
        print("✅ Email sent successfully!")
    except Exception as e:
        print(f"❌ Failed to send email: {e}")

def send_whatsapp_notification(message, recipient):
    try:
        client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
        client.messages.create(
            from_='whatsapp:' + TWILIO_PHONE,
            body=message,
            to='whatsapp:' + recipient
        )
        print("✅ WhatsApp message sent successfully!")
    except Exception as e:
        print(f"❌ Failed to send WhatsApp message: {e}")
