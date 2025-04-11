import os
import csv
from datetime import datetime

def log_price(from_city, to_city, price, target_price, status):
    log_file = "logs/flight_prices.csv"
    os.makedirs("logs", exist_ok=True)

    file_exists = os.path.isfile(log_file)
    with open(log_file, mode="a", newline="") as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["Timestamp", "From", "To", "Current Price", "Target Price", "Status"])
        writer.writerow([
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            from_city,
            to_city,
            price,
            target_price,
            status
        ])

