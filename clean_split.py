import pandas as pd
from sklearn.model_selection import train_test_split

# Load the dataset
data_path = r"C:\Users\gurus\project\phishing\enhanced_dataset.csv"  # Adjust if needed
data = pd.read_csv(data_path)

# Remove duplicate rows
data = data.drop_duplicates().reset_index(drop=True)
print(f"Dataset after removing duplicates: {data.shape[0]} rows")

# Shuffle the dataset
data = data.sample(frac=1, random_state=42).reset_index(drop=True)

# Split into features (X) and target (y)
X = data.drop(columns=["Label"])  # Replace 'Label' if your target column has another name
y = data["Label"]

# Split into training and testing sets (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

# Check for overlap
common_rows = pd.merge(X_train, X_test, how="inner")
print(f"Number of common rows between train and test: {len(common_rows)}")

# Save the splits to new CSV files if no overlap
if len(common_rows) == 0:
    X_train.to_csv(r"C:\Users\gurus\project\phishing\X_train.csv", index=False)
    X_test.to_csv(r"C:\Users\gurus\project\phishing\X_test.csv", index=False)
    y_train.to_csv(r"C:\Users\gurus\project\phishing\y_train.csv", index=False)
    y_test.to_csv(r"C:\Users\gurus\project\phishing\y_test.csv", index=False)
    print("Data splitting complete. New training and testing sets created!")
else:
    print("Overlap still exists. Please review the dataset.")

