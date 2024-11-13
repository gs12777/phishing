import requests

# Open Page Rank API details
openpagerank_api_key = "0gcgcskoskwggwwwcwgoo0wcw4kg8o0o88osk8o4"
openpagerank_endpoint = "https://openpagerank.com/api/v1.0/getPageRank"

def get_legitimate_urls():
    popular_sites = [
        "example.com", "wikipedia.org", "amazon.com", "youtube.com", "facebook.com"
        # Add more popular domain names to increase dataset size
    ]
    
    legitimate_urls = []
    headers = {"API-OPR": openpagerank_api_key}

    for domain in popular_sites:
        try:
            response = requests.get(openpagerank_endpoint, headers=headers, params={"domains[]": domain})
            if response.status_code == 200:
                data = response.json()
                if data["status_code"] == 200 and data["response"]:
                    legitimate_urls.append(domain)
        except Exception as e:
            print(f"Error with domain {domain}: {e}")
    
    # Save the URLs to a file
    with open("legitimate_urls.txt", "w") as f:
        for url in legitimate_urls:
            f.write(url + "\n")
        print("Legitimate URLs saved successfully.")

if __name__ == "__main__":
    get_legitimate_urls()

