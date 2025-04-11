import requests
from config import SKYSCANNER_API_KEY
from notifier import send_notification
from log_price import log_price

def get_user_input():
    from_city = input("Enter source airport code (e.g., DEL): ").strip().upper()
    to_city = input("Enter destination airport code (e.g., BOM): ").strip().upper()
    date = input("Enter date of travel (YYYY-MM-DD): ").strip()
    target_price = float(input("Enter your target price (INR): "))
    return {
        "from": from_city,
        "to": to_city,
        "date": date,
        "target_price": target_price
    }

def check_flight_price(route):
    # Simulated API response
    print(f"\nChecking flight from {route['from']} to {route['to']} on {route['date']}...")
    current_price = 4999  # Simulated price (replace with real API response)

    # Logging the price
    status = "Below Target" if current_price <= route['target_price'] else "Above Target"
    log_price(route['from'], route['to'], current_price, route['target_price'], status)

    # Notify if below target
    if current_price <= route['target_price']:
        message = f"🎉 Flight price drop alert!\nFrom: {route['from']} To: {route['to']}\nDate: {route['date']}\nCurrent Price: ₹{current_price} (Target: ₹{route['target_price']})"
        send_notification(message)

if __name__ == "__main__":
    route_info = get_user_input()
    check_flight_price(route_info)
