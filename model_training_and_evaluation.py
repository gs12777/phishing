import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns

# Step 1: Load the training and testing datasets
X_train = pd.read_csv("X_train.csv")
y_train = pd.read_csv("y_train.csv").squeeze()  # Ensure y_train is a Series
X_test = pd.read_csv("X_test.csv")
y_test = pd.read_csv("y_test.csv").squeeze()  # Ensure y_test is a Series

# Step 2: Train Random Forest Classifier
print("Training Random Forest Classifier...")
rf_model = RandomForestClassifier(random_state=42)
rf_model.fit(X_train, y_train)

# Evaluate Random Forest
print("Evaluating Random Forest...")
rf_predictions = rf_model.predict(X_test)
rf_accuracy = accuracy_score(y_test, rf_predictions)
print(f"Random Forest Accuracy: {rf_accuracy}")
print("Classification Report:")
print(classification_report(y_test, rf_predictions))

# Confusion Matrix for Random Forest
rf_cm = confusion_matrix(y_test, rf_predictions)
plt.figure(figsize=(6, 4))
sns.heatmap(rf_cm, annot=True, fmt='d', cmap="Blues", xticklabels=["Legitimate", "Phishing"], yticklabels=["Legitimate", "Phishing"])
plt.title("Random Forest Confusion Matrix")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.savefig("random_forest_cm.png")
plt.show()

# Step 3: Train Neural Network Classifier
print("Training Neural Network Classifier...")
nn_model = MLPClassifier(hidden_layer_sizes=(100, 50), max_iter=300, random_state=42)
nn_model.fit(X_train, y_train)

# Evaluate Neural Network
print("Evaluating Neural Network...")
nn_predictions = nn_model.predict(X_test)
nn_accuracy = accuracy_score(y_test, nn_predictions)
print(f"Neural Network Accuracy: {nn_accuracy}")
print("Classification Report:")
print(classification_report(y_test, nn_predictions))

# Confusion Matrix for Neural Network
nn_cm = confusion_matrix(y_test, nn_predictions)
plt.figure(figsize=(6, 4))
sns.heatmap(nn_cm, annot=True, fmt='d', cmap="Greens", xticklabels=["Legitimate", "Phishing"], yticklabels=["Legitimate", "Phishing"])
plt.title("Neural Network Confusion Matrix")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.savefig("neural_network_cm.png")
plt.show()

print("Training and evaluation complete!")
