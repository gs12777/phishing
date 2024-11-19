import pandas as pd
from sklearn.preprocessing import MinMaxScaler

# Load the dataset
data_path = r"C:\Users\gurus\project\phishing\shuffled_dataset.csv"
data = pd.read_csv(data_path)

# Define the normalizer function
def normalize_features(df, columns_to_normalize):
    scaler = MinMaxScaler()
    df[columns_to_normalize] = scaler.fit_transform(df[columns_to_normalize])
    return df

# Specify the columns to normalize
features_to_normalize = ['url_length', 'num_dots', 'num_slashes', 'num_digits', 'has_https', 'has_suspicious_word']

# Normalize the data
data_normalized = normalize_features(data, features_to_normalize)

# Save the normalized dataset
normalized_dataset_path = r"C:\Users\gurus\project\phishing\normalized_dataset.csv"
data_normalized.to_csv(normalized_dataset_path, index=False)
print(f"Normalized dataset saved at: {normalized_dataset_path}")
