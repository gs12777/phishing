import requests
import json
import csv
import os
import pandas as pd

# Define the path to store collected data and the domains CSV
output_path = "C:\\Users\\gurus\\project\\phishing\\url_data.csv"
domains_file_path = "C:\\Users\\gurus\\project\\phishing\\top_domains.csv"

# Define headers for the CSV file
headers = ["URL", "Label"]

# API keys (replace these placeholders with actual keys if necessary)
OPEN_PAGE_RANK_API_KEY = "0gcgcskoskwggwwwcwgoo0wcw4kg8o0o88osk8o4"

# 1. Fetch phishing URLs from OpenPhish
def fetch_phishing_urls():
    url = "https://openphish.com/feed.txt"  # OpenPhish URL feed
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check if the request was successful
        phishing_urls = response.text.splitlines()
        print(f"Fetched {len(phishing_urls)} phishing URLs.")
        return phishing_urls
    except requests.RequestException as e:
        print("Error fetching phishing URLs:", e)
        return []

# 2. Fetch legitimate URLs using Open Page Rank API
def fetch_legitimate_urls():
    url = "https://openpagerank.com/api/v1.0/getPageRank"
    
    # Read domains from the CSV file
    try:
        domains_df = pd.read_csv(domains_file_path)
        domains = domains_df["Domain"].head(500).tolist()  # Assumes 'Domain' is the column name
    except Exception as e:
        print(f"Error reading domains file: {e}")
        return []

    legitimate_urls = []
    for domain in domains:
        try:
            response = requests.get(
                url,
                params={"domains[]": domain},
                headers={"API-OPR": OPEN_PAGE_RANK_API_KEY}
            )
            response.raise_for_status()
            data = response.json()
            for result in data.get("response", []):
                if result["page_rank_integer"] > 3:
                    legitimate_urls.append(f"https://{result['domain']}")
            print(f"Fetched legitimate URLs from {domain}.")
        except requests.RequestException as e:
            print(f"Error fetching URLs for {domain}: {e}")
    
    print(f"Fetched {len(legitimate_urls)} legitimate URLs.")
    return legitimate_urls

# 3. Save URLs to CSV
def save_urls_to_csv(phishing_urls, legitimate_urls):
    if not os.path.exists(output_path):
        with open(output_path, "w", newline="") as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(headers)  # Write headers

    with open(output_path, "a", newline="") as csv_file:
        writer = csv.writer(csv_file)
        for url in phishing_urls:
            writer.writerow([url, "phishing"])
        for url in legitimate_urls:
            writer.writerow([url, "legitimate"])

    print(f"Saved {len(phishing_urls) + len(legitimate_urls)} URLs to {output_path}")

# 4. Main function to run the data collection
def main():
    phishing_urls = fetch_phishing_urls()
    legitimate_urls = fetch_legitimate_urls()
    save_urls_to_csv(phishing_urls, legitimate_urls)

if __name__ == "__main__":
    main()


