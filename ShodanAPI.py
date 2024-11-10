# Darlene Lopez
# CIS 131
# This program imports Shodan to view addresses from local organizations and gas

import shodan
from datetime import datetime

# Shodan API key
SHODAN_API_KEY = 'bIWOjW69QxF96gvhb4a1vNN7JgyjPYQ4'

# Initialize the Shodan API client
api = shodan.Shodan(SHODAN_API_KEY)

# Search query for in-tank inventory information in Arizona
query = '"in-tank inventory" state:"AZ"'

try:
    # Get the current date and time
    current_datetime = datetime.now().strftime("%b %d, %Y %I:%M %p")

    # Search Shodan for devices matching the query
    results = api.search(query)

    print(f"Total Results Found: {results['total']}\n")

    # Iterate over each result
    for idx, result in enumerate(results['matches'], start=1):
        ip = result.get('ip_str', 'N/A')
        location = result.get('location', {})
        city = location.get('city', 'N/A')
        state = location.get('region_code', 'N/A')
        organization = result.get('org', 'N/A')

        # Mocked sample in-tank inventory data for formatting purposes
        # Replace these values with actual data if available in Shodan results
        tank_data = [
            {"TANK": "1", "PRODUCT": "OFF-ROAD DIESEL", "VOLUME_TC": "2785", "VOLUME": "2806", "ULLAGE": "7504",
             "HEIGHT": "30.10", "WATER": "0.00", "TEMP": "75.74"},
            {"TANK": "2", "PRODUCT": "TEXACO UNLEADED", "VOLUME_TC": "3032", "VOLUME": "7200", "ULLAGE": "63.15",
             "HEIGHT": "63.15", "WATER": "0.00", "TEMP": "75.23"},
            {"TANK": "3", "PRODUCT": "CARDLOCK UNLEADED", "VOLUME_TC": "7519", "VOLUME": "7598", "ULLAGE": "2712",
             "HEIGHT": "65.63", "WATER": "0.00", "TEMP": "74.83"},
            {"TANK": "4", "PRODUCT": "ULSD DIESEL", "VOLUME_TC": "3214", "VOLUME": "7037", "ULLAGE": "61.76",
             "HEIGHT": "61.76", "WATER": "0.00", "TEMP": "78.33"},
            {"TANK": "5", "PRODUCT": "PREMIUM", "VOLUME_TC": "1190", "VOLUME": "3820", "ULLAGE": "67.87",
             "HEIGHT": "67.87", "WATER": "0.00", "TEMP": "74.95"},
            {"TANK": "6", "PRODUCT": "DEF TANK", "VOLUME_TC": "838", "VOLUME": "843", "ULLAGE": "857",
             "HEIGHT": "33.52", "WATER": "0.00", "TEMP": "71.20"},
        ]

        # Display header with real-time date and time
        print("I20100")
        print(current_datetime)
        print()
        print(f"{organization}")
        print(f"{ip}")
        print(f"{city},{state}")
        print()
        print("IN-TANK INVENTORY")
        print()

        # Print tank data in table format
        print("TANK PRODUCT               VOLUME TC  VOLUME  ULLAGE  HEIGHT  WATER  TEMP")
        for tank in tank_data:
            print(
                f"{tank['TANK']: <5} {tank['PRODUCT']: <20} {tank['VOLUME_TC']: <7} {tank['VOLUME']: <7} {tank['ULLAGE']: <7} {tank['HEIGHT']: <7} {tank['WATER']: <6} {tank['TEMP']: <5}")

        print("-" * 40)  # Separator for each result

except shodan.APIError as e:
    print(f"Shodan API Error: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
