import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
# Load normalized dataset
data_path = r"C:\Users\gurus\project\phishing\normalized_dataset.csv"
data = pd.read_csv(data_path)

# Features and target
X = data.drop(columns=["Label"])  # Replace "Label" if target column is named differently
y = data["Label"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
X_no_slashes = X.drop(columns=["num_slashes"])

# Reset indices to ensure alignment
X_no_slashes = X_no_slashes.reset_index(drop=True)
y = y.reset_index(drop=True)

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(X_no_slashes, y, test_size=0.2, random_state=42)

# Train a new Random Forest model without 'num_slashes'
rf_model_no_slashes = RandomForestClassifier(random_state=42, n_estimators=100)
rf_model_no_slashes.fit(X_train, y_train)

# Test the model
rf_no_slashes_predictions = rf_model_no_slashes.predict(X_test)
rf_no_slashes_accuracy = accuracy_score(y_test, rf_no_slashes_predictions)

print("Random Forest Accuracy without 'num_slashes':", rf_no_slashes_accuracy)

# Feature Importance Plot without 'num_slashes'
importances_no_slashes = rf_model_no_slashes.feature_importances_
feature_names_no_slashes = X_train.columns

plt.figure(figsize=(10, 6))
plt.barh(feature_names_no_slashes, importances_no_slashes, color="salmon")
plt.xlabel("Feature Importance")
plt.ylabel("Feature")
plt.title("Random Forest Feature Importance (Without 'num_slashes')")
plt.show()