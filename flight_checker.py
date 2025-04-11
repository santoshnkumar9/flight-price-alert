from config import SKYSCANNER_API_KEY
from notifier import send_notification
from log_price import log_price

def check_flight_price(route):
    print(f"\nChecking flight from {route['from']} to {route['to']} on {route['date']}...")
    current_price = 4999  # Simulated price (replace with real API later)

    status = "Below Target" if current_price <= route['target_price'] else "Above Target"
    log_price(route['from'], route['to'], current_price, route['target_price'], status)

    return current_price
