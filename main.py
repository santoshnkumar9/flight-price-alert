from flight_checker import check_flight_price
from notifier import send_notification
from config import ROUTE, TARGET_PRICE

def main():
    current_price = check_flight_price(ROUTE)
    if current_price <= TARGET_PRICE:
        send_notification(current_price, ROUTE)

if __name__ == "__main__":
    main()
