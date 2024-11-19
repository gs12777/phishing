import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.neural_network import MLPClassifier

# Paths to the cleaned datasets
X_train_path = r"C:\Users\gurus\project\phishing\X_train.csv"
X_test_path = r"C:\Users\gurus\project\phishing\X_test.csv"
y_train_path = r"C:\Users\gurus\project\phishing\y_train.csv"
y_test_path = r"C:\Users\gurus\project\phishing\y_test.csv"

# Load the datasets
X_train = pd.read_csv(X_train_path)
X_test = pd.read_csv(X_test_path)
y_train = pd.read_csv(y_train_path).squeeze()  # Ensure it's a Series
y_test = pd.read_csv(y_test_path).squeeze()

# Random Forest Model
rf_model = RandomForestClassifier(random_state=42)
rf_model.fit(X_train, y_train)
rf_predictions = rf_model.predict(X_test)
rf_accuracy = accuracy_score(y_test, rf_predictions)
print(f"Random Forest Accuracy: {rf_accuracy}")

# Neural Network Model
nn_model = MLPClassifier(hidden_layer_sizes=(50, 30), random_state=42, max_iter=500)
nn_model.fit(X_train, y_train)
nn_predictions = nn_model.predict(X_test)
nn_accuracy = accuracy_score(y_test, nn_predictions)
print(f"Neural Network Accuracy: {nn_accuracy}")
