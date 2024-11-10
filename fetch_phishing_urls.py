import requests

# URLhaus API endpoint for recent URLs
url = "https://urlhaus-api.abuse.ch/v1/urls/recent/"

# Make the GET request to fetch recent URLs
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    urls = response.json()  # Parse the JSON response
    for url_data in urls['urls']:
        print(url_data['url'])  # Print each phishing URL
else:
    print(f"Failed to retrieve data: {response.status_code}")
