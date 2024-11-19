import pandas as pd
import re

def extract_features(url):
    return {
        'URL_Length': len(url),
        'Num_Special_Chars': len(re.findall(r'[!@#$%^&*()_\-+=~`]', url)),
        'Has_IP': 1 if re.match(r'\d+\.\d+\.\d+\.\d+', url) else 0,
        'Keyword_Flag': 1 if any(keyword in url.lower() for keyword in ['login', 'secure', 'verify']) else 0
    }

df = pd.read_csv('url_data.csv')
features = df['URL'].apply(extract_features)
features_df = pd.DataFrame(features.tolist())
df = pd.concat([df, features_df], axis=1)
df.to_csv('final_dataset_with_features.csv', index=False)
