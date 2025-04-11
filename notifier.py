from config import WHATSAPP_NUMBER, EMAIL, TWILIO_SID, TWILIO_AUTH_TOKEN, EMAIL_PASSWORD
from twilio.rest import Client
import smtplib

def send_notification(price, route):
    message = f"🔔 Flight price drop alert!\nFrom {route['from']} to {route['to']}\nPrice: ₹{price}"

    # WhatsApp notification
    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
    client.messages.create(
        body=message,
        from_='whatsapp:+14155238886',
        to=f'whatsapp:{WHATSAPP_NUMBER}'
    )

    # Email notification
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(EMAIL, EMAIL_PASSWORD)
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs=EMAIL,
            msg=f"Subject:Flight Price Alert!\n\n{message}"
        )
