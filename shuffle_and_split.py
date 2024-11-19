import pandas as pd
from sklearn.model_selection import train_test_split

# Load the dataset
file_path = r"C:\Users\gurus\project\phishing\enhanced_dataset.csv"  # Replace with your actual dataset path
data = pd.read_csv(file_path)

# Shuffle the dataset
data = data.sample(frac=1, random_state=42).reset_index(drop=True)

# Save the shuffled dataset for reference
shuffled_path = r"C:\Users\gurus\project\phishing\shuffled_data.csv"
data.to_csv(shuffled_path, index=False)
print(f"Shuffled dataset saved at: {shuffled_path}")

# Split into features (URLs) and labels (phishing or legitimate)
X = data['URL']  # Assuming the column for URLs is named 'URL'
y = data['Label']  # Assuming the column for labels is named 'Label'

# Split into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

# Combine X and y for train and test into DataFrames
train_data = pd.DataFrame({'URL': X_train, 'Label': y_train})
test_data = pd.DataFrame({'URL': X_test, 'Label': y_test})

# Save the training and testing datasets
train_path = r"C:\Users\gurus\project\phishing\train_data.csv"
test_path = r"C:\Users\gurus\project\phishing\test_data.csv"

train_data.to_csv(train_path, index=False)
test_data.to_csv(test_path, index=False)

print(f"Training dataset saved at: {train_path}")
print(f"Testing dataset saved at: {test_path}")
