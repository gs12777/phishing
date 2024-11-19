import pandas as pd
from sklearn.model_selection import train_test_split

# Load the dataset
data = pd.read_csv("shuffled_dataset.csv")  # Update the path if needed

# Define features (X) and target (y)
X = data.drop(columns=["Label"])  # Drop the target column
y = data["Label"]  # Keep only the target column

# Split the data into training and testing sets (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Print dataset information
print("Data successfully split into training and testing sets.")
print("Training set size:", len(X_train))
print("Testing set size:", len(X_test))

# Save training and testing data to CSV files for future use
X_train.to_csv("X_train.csv", index=False)
X_test.to_csv("X_test.csv", index=False)
y_train.to_csv("y_train.csv", index=False)
y_test.to_csv("y_test.csv", index=False)

print("Training and testing sets saved as CSV files.")
