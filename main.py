from flight_checker import check_flight_price
from log_price import log_price
from notifier import send_notification

# 🔸 Step 1: Get dynamic user inputs
from_city = input("Enter departure airport code (e.g. DEL): ").strip().upper()
to_city = input("Enter destination airport code (e.g. BOM): ").strip().upper()
date = input("Enter travel date (YYYY-MM-DD): ").strip()
target_price = float(input("Enter your target price (INR): "))

# 🔸 Step 2: Get recipient info
email_receiver = input("Enter email for notifications: ").strip()
whatsapp_receiver = input("Enter WhatsApp number (with +country_code): ").strip()

# 🔸 Step 3: Prepare route dict
route = {
    "from": from_city,
    "to": to_city,
    "date": date,
    "target_price": target_price
}

# 🔸 Step 4: Check price
current_price = check_flight_price(route)

# 🔸 Step 5: Log results
status = "Below Target 🎉" if current_price <= target_price else "Above Target ❌"
log_price(from_city, to_city, current_price, target_price, status)

# 🔸 Step 6: Notify if needed
if current_price <= target_price:
    message = (
        f"✈️ Price Drop Alert!\n\n"
        f"{from_city} ➡️ {to_city} on {date}\n"
        f"Current Price: ₹{current_price}\n"
        f"Your Target: ₹{target_price}\n\n"
        f"Book now before it goes up! 💸"
    )
    send_notification(message, email_receiver, whatsapp_receiver)
else:
    print("ℹ️ Price is above target. No notification sent.")
