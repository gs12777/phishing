import pandas as pd
import re
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

# Load the dataset
dataset_path = r"C:\Users\gurus\project\phishing\url_data.csv"
data = pd.read_csv(dataset_path)

# Feature Engineering
def has_https(url):
    return int(url.startswith("https://"))

def count_special_chars(url):
    return sum(1 for char in url if char in ['@', '/', '=', '&', '%'])

def count_dots(url):
    return url.count('.')

def contains_ip(url):
    pattern = r'(\d{1,3}\.){3}\d{1,3}'
    return int(bool(re.search(pattern, url)))

data['URL_Length'] = data['URL'].apply(len)
data['Has_HTTPS'] = data['URL'].apply(has_https)
data['Special_Char_Count'] = data['URL'].apply(count_special_chars)
data['Dot_Count'] = data['URL'].apply(count_dots)
data['Contains_IP'] = data['URL'].apply(contains_ip)

# Save Enhanced Dataset
enhanced_dataset_path = r"C:\Users\gurus\project\phishing\enhanced_dataset.csv"
data.to_csv(enhanced_dataset_path, index=False)

# Visualize Features
sns.histplot(data['URL_Length'], kde=True, bins=30)
plt.title("Distribution of URL Length")
plt.show()

sns.histplot(data['Dot_Count'], kde=True, bins=10)
plt.title("Distribution of Dot Count")
plt.show()

# Ensure only numeric columns are used for correlation
numeric_data = data.select_dtypes(include=['number'])

# Check Correlation
correlation_matrix = numeric_data.corr()
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm")
plt.title("Feature Correlation")
plt.show()

# Split Dataset
X = data.drop(columns=['Label', 'URL'])  # Exclude non-numeric columns
y = data['Label']  # Target column
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print("Training Set Size:", X_train.shape)
print("Testing Set Size:", X_test.shape)
