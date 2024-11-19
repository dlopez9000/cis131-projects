# Darlene Lopez
# CIS 131
# This program imports Shodan, GmailAPI, and sinch sms to send information to the user

import ezgmail
import requests
import shodan
from datetime import datetime

# Gmail API Initialization
try:
    ezgmail.init()
except Exception as e:
    print(f"Error initializing Gmail: {e}")

# Shodan API Key
SHODAN_API_KEY = 'bIWOjW69QxF96gvhb4a1vNN7JgyjPYQ4'
api = shodan.Shodan(SHODAN_API_KEY)

# Sinch API credentials
SINCH_SERVICE_PLAN_ID = 'f79695d9-4dd4-4c2f-be46-797713da6f6f'
SINCH_API_KEY = 'Pxjs9JCDAl~a56JYlIgtOCdu~G'

# Search query for in-tank inventory information in Arizona
query = '"in-tank inventory" state:"AZ"'


def send_sms(phone_number, message):
    """Send SMS using Sinch API."""
    url = f"https://sms.api.sinch.com/xms/v1/{SINCH_SERVICE_PLAN_ID}/batches"
    headers = {
        "Authorization": f"Bearer {SINCH_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "from": "SenderID",
        "to": [phone_number],
        "body": message
    }

    response = requests.post(url, headers=headers, json=payload)
    if response.status_code == 201:
        print("SMS sent successfully!")
    else:
        print(f"Failed to send SMS: {response.status_code} {response.text}")


def send_email_report(subject, content):
    """Send email report using Gmail."""
    try:
        ezgmail.send('dlopez232@mail.pima.edu', subject, content)
        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")


def check_gas_gauges():
    """Search for gas gauges and send notifications."""
    try:
        # Get the current date and time
        current_datetime = datetime.now().strftime("%b %d, %Y %I:%M %p")

        # Search Shodan for devices matching the query
        results = api.search(query)

        print(f"Total Results Found: {results['total']}\n")

        # Prepare the email content
        email_content = f"Shodan Gas Gauge Report - {current_datetime}\n\n"
        alert_triggered = False

        for idx, result in enumerate(results['matches'], start=1):
            ip = result.get('ip_str', 'N/A')
            location = result.get('location', {})
            city = location.get('city', 'N/A')
            state = location.get('region_code', 'N/A')
            organization = result.get('org', 'N/A')

            # Mocked sample in-tank inventory data
            tank_data = [
                {"TANK": "1", "PRODUCT": "OFF-ROAD DIESEL", "VOLUME_TC": "2785", "VOLUME": "2806", "ULLAGE": "7504",
                 "HEIGHT": "30.10", "WATER": "0.00", "TEMP": "75.74"},
                {"TANK": "2", "PRODUCT": "TEXACO UNLEADED", "VOLUME_TC": "3032", "VOLUME": "7200", "ULLAGE": "63.15",
                 "HEIGHT": "63.15", "WATER": "0.00", "TEMP": "75.23"},
                # Add other tank data as needed
            ]

            # Add to email content
            email_content += f"{organization}\n{ip}\n{city}, {state}\n\n"
            email_content += "IN-TANK INVENTORY\n\n"
            email_content += "TANK PRODUCT               VOLUME TC  VOLUME  ULLAGE  HEIGHT  WATER  TEMP\n"
            for tank in tank_data:
                email_content += (
                    f"{tank['TANK']: <5} {tank['PRODUCT']: <20} {tank['VOLUME_TC']: <7} {tank['VOLUME']: <7} "
                    f"{tank['ULLAGE']: <7} {tank['HEIGHT']: <7} {tank['WATER']: <6} {tank['TEMP']: <5}\n"
                )
            email_content += "-" * 40 + "\n"

            # Trigger SMS alert if a gas gauge is found in Phoenix
            if city == "Phoenix":
                alert_triggered = True

        # Send email report
        send_email_report("Shodan Gas Gauge Report", email_content)

        # Send SMS alert
        if alert_triggered:
            send_sms('6194849025', 'ALERT: Gas gauge exposed in Phoenix, AZ!')
        else:
            send_sms('6194849025', 'Internet Gas Gauge in AZ report delivered to email')

    except shodan.APIError as e:
        print(f"Shodan API Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# Main function
def main():
    check_gas_gauges()


# Run the main function
if __name__ == "__main__":
    main()
