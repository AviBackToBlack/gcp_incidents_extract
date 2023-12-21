#!/usr/bin/env python

import requests
import json

# Constants
# Replace 'your_project_id' with your actual project ID from Google Cloud Platform.
# You can find your project ID in the Google Cloud Console.
PROJECT_ID = 'your_project_id'

# Replace 'your_authorization', 'your_key' and 'your_cookie'
# with information obtained from requests to Google Cloud Console.
# To retrieve this information:
# 1. Log in to the Google Cloud Console.
# 2. Navigate to the Monitoring section and open the network tab in your browser's development tools.
# 3. Trigger an incident retrieval in the console and look for the outgoing API request.
# 4. Inspect the request headers and copy the value of the parameters mentioned.
# Note: This parameters are sensitive and should be kept secure.
AUTHORIZATION = 'your_authorization'
KEY = 'your_key'
COOKIE = 'your_cookie'

# Replace 'YYYY-MM-DD' with the time range you are looking for
DATE_FROM = 'YYYY-MM-DD'
DATE_TO = 'YYYY-MM-DD'

BASE_URL = f'https://monitoring.clients6.google.com/v3/projects/{PROJECT_ID}/incidents'
PAGE_SIZE = 200

def get_incidents(next_page_token=None):
    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.9',
        'Authorization': AUTHORIZATION,
        'Origin': 'https://console.cloud.google.com',
        'Referer': 'https://console.cloud.google.com/',
        'Cookie': COOKIE,
    }

    url = f"{BASE_URL}?filter=(open_time%3E=%22{DATE_FROM}T00:00:00Z%22%20AND%20open_time%3C=%22{DATE_TO}T23:59:59Z%22)&pageSize={PAGE_SIZE}&key={KEY}"
    if next_page_token:
        url += f"&pageToken={next_page_token}"
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Failed to fetch data: {response.status_code}")

def main():
    incidents = []
    next_page_token = None
    page_number = 1

    while True:
        try:
            print(f"Fetching page number {page_number}...")
            data = get_incidents(next_page_token)
            next_page_token = data.get('nextPageToken')
            incidents.extend(data['incidents'])
            page_number += 1

            if not next_page_token:
                break
        except Exception as e:
            print(f"Error: {e}")
            break

    with open(f'{PROJECT_ID}_incidents.json', 'w') as file:
        json.dump(incidents, file, indent=4)

if __name__ == "__main__":
    main()
