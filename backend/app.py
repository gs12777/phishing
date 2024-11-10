from flask import Flask, request, jsonify
from flask_cors import CORS
import re

app = Flask(__name__)
CORS(app)  # This allows cross-origin requests

def check_if_safe(url):
    # Ensure the URL has the scheme (http:// or https://)
    if not re.match(r'^https?://', url):
        if not url.startswith('www.'):
            # Invalid URL format
            print(f"Invalid URL format: {url}")  # Log the invalid URL for debugging
            return 'Invalid URL format. Please include "http://" or "https://".', 400
        # If the URL starts with 'www.', prepend 'http://'
        url = 'http://' + url

    # Check for suspicious keywords in the URL (expand this as needed)
    suspicious_keywords = ['phishing', 'login', 'secure', 'bank', 'verify']
    if any(keyword in url.lower() for keyword in suspicious_keywords):
        return 'The URL is potentially dangerous.', 200

    # If it's safe or no suspicious keywords found
    return 'The URL is safe.', 200

@app.route('/api/check', methods=['POST'])
def check_url():
    try:
        data = request.json
        url = data.get('url', '').strip()

        if not url:
            return jsonify({'message': 'URL is required'}), 400

        # Check if URL is safe or potentially dangerous
        message, status_code = check_if_safe(url)

        # Debug log to check response
        print(f"Response message: {message} with status code {status_code}")

        return jsonify({'message': message}), status_code
    except Exception as e:
        # Log the error for debugging
        print(f"Error occurred: {str(e)}")
        return jsonify({'message': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
