import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from config import EMAIL_SENDER, EMAIL_PASSWORD, EMAIL_RECEIVER
from config import TWILIO_SID, TWILIO_AUTH_TOKEN, TWILIO_PHONE, YOUR_PHONE
from twilio.rest import Client

def send_notification(message):
    send_email_notification(message)
    send_whatsapp_notification(message)

def send_email_notification(message):
    try:
        msg = MIMEMultipart()
        msg['From'] = EMAIL_SENDER
        msg['To'] = EMAIL_RECEIVER
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

def send_whatsapp_notification(message):
    try:
        client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
        client.messages.create(
            from_='whatsapp:' + TWILIO_PHONE,
            body=message,
            to='whatsapp:' + YOUR_PHONE
        )
        print("✅ WhatsApp message sent successfully!")
    except Exception as e:
        print(f"❌ Failed to send WhatsApp message: {e}")
