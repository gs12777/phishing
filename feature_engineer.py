import pandas as pd
import re

# Define a function to extract features from URLs
def extract_features(url):
    return {
        "url_length": len(url),
        "num_dots": url.count('.'),
        "num_slashes": url.count('/'),
        "num_digits": sum(c.isdigit() for c in url),
        "has_https": 1 if "https" in url else 0,
        "has_suspicious_word": 1 if any(keyword in url.lower() for keyword in ["login", "verify", "update", "secure"]) else 0
    }

# Load the raw dataset with URLs
data = pd.read_csv("url_data.csv")  # Replace with your file name

# Apply feature extraction
features = data["URL"].apply(lambda x: pd.Series(extract_features(x)))

# Add the target column back
features["Label"] = data["Label"]  # Replace 'Label' with the correct column name in your dataset

# Save the enhanced dataset
features.to_csv("enhanced_dataset.csv", index=False)

print("Feature engineering completed. Enhanced dataset saved as 'enhanced_dataset.csv'.")
