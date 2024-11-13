import requests
import socket
import json
import re
from urllib.parse import urlparse

# Replace with your OpenPhish and AbuseIPDB API keys
OPENPHISH_API_URL = "https://openphish.com/feed.txt"
ABUSEIPDB_API_KEY = "your_abuseipdb_api_key"
ABUSEIPDB_API_URL = "https://api.abuseipdb.com/api/v2/check"

# Function to fetch phishing URLs from OpenPhish
def fetch_phishing_urls():
    try:
        response = requests.get(OPENPHISH_API_URL)
        response.raise_for_status()  # Will raise HTTPError for bad responses
        phishing_urls = response.text.splitlines()
        return phishing_urls
    except requests.exceptions.RequestException as e:
        print(f"Error fetching phishing URLs: {e}")
        return []

# Function to resolve domain to IP address, with special handling for non-standard URLs
def get_ip_from_url(url):
    # Skip IPFS or other non-standard URLs
    if "ipfs.io" in url or "onion" in url:
        print(f"Skipping non-resolvable URL: {url}")
        return None
    
    try:
        # Parse the domain from the URL
        parsed_url = urlparse(url)
        domain = parsed_url.netloc
        
        # Check if domain exists before trying to resolve it
        if not domain:
            print(f"Invalid URL, skipping: {url}")
            return None
        
        # Attempt to resolve the domain to an IP
        ip = socket.gethostbyname(domain)
        return ip
    except socket.gaierror as e:
        print(f"Error resolving {url}: {e}")
        return None
    except UnicodeError as e:
        print(f"Error with URL '{url}': {e}. Skipping URL.")
        return None

# Function to check if an IP is flagged by AbuseIPDB
def check_ip_abuse(ip):
    headers = {
        'Key': ABUSEIPDB_API_KEY,
        'Accept': 'application/json'
    }
    
    params = {
        'ipAddress': ip,
    }
    
    try:
        response = requests.get(ABUSEIPDB_API_URL, headers=headers, params=params)
        response.raise_for_status()  # Will raise HTTPError for bad responses
        data = response.json()
        
        # Check if the IP has a "reputation" score indicating malicious behavior
        if data['data']['abuseConfidenceScore'] > 50:
            return True  # Malicious IP
        else:
            return False  # Safe IP
    except requests.exceptions.RequestException as e:
        print(f"Error checking IP {ip} with AbuseIPDB: {e}")
        return None

# Function to check phishing URLs and IPs
def check_phishing_and_ip():
    phishing_urls = fetch_phishing_urls()
    
    if not phishing_urls:
        print("No phishing URLs fetched.")
        return
    
    for url in phishing_urls:
        print(f"Checking URL: {url}")
        
        # Extract IP address from URL
        ip = get_ip_from_url(url)
        
        if ip:
            print(f"IP address for {url}: {ip}")
            
            # Check the IP with AbuseIPDB
            is_abused = check_ip_abuse(ip)
            
            if is_abused is None:
                print(f"Could not check IP {ip}")
            elif is_abused:
                print(f"IP {ip} is flagged as malicious!")
            else:
                print(f"IP {ip} is safe.")
        else:
            print(f"Could not resolve IP for {url}")
        
        print("-" * 50)  # Separator for readability

# Main function to run the checks
if __name__ == "__main__":
    check_phishing_and_ip()
