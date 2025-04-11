import requests
from config import SKYSCANNER_API_KEY

def check_flight_price(route):
    # This is a simulated response. You’ll replace it with a real API call.
    print(f"Checking flight price for: {route['from']} to {route['to']} on {route['date']}")
    return 4999  # Simulated price in INR
