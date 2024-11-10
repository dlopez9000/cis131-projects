# Darlene Lopez
# CIS 131
# This program imports Shodan to view addresses from local organizations 

import shodan

# Shodan API key
SHODAN_API_KEY = 'bIWOjW69QxF96gvhb4a1vNN7JgyjPYQ4'

# Initialize the Shodan API
api = shodan.Shodan(SHODAN_API_KEY)

# Search query
query = '"in-tank inventory" state:"AZ"'

try:
    # Perform the search
    results = api.search(query)

    print(f"Total Results Found: {results['total']}\n")

    # Iterate through the matches and print desired data elements
    for idx, result in enumerate(results['matches'], start=1):
        ip = result.get('ip_str', 'N/A')
        port = result.get('port', 'N/A')
        hostnames = result.get('hostnames', [])
        org = result.get('org', 'N/A')
        location = result.get('location', {})
        city = location.get('city', 'N/A')
        region_code = location.get('region_code', 'N/A')
        country_code = location.get('country_code', 'N/A')
        isp = result.get('isp', 'N/A')
        last_update = result.get('last_update', 'N/A')

        print(f"Result {idx}:")
        print(f"  IP Address      : {ip}")
        print(f"  Port            : {port}")
        print(f"  Hostnames       : {', '.join(hostnames) if hostnames else 'N/A'}")
        print(f"  Organization    : {org}")
        print(f"  Location        : {city}, {region_code}, {country_code}")
        print(f"  ISP             : {isp}")
        print(f"  Last Update     : {last_update}")
        print("-" * 40)

except shodan.APIError as e:
    print(f"Shodan API Error: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
