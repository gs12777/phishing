import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.preprocessing import StandardScaler

# Load your dataset
data = pd.read_csv("normalized_dataset.csv")

# Remove 'num_slashes' feature
data = data.drop(columns=['num_slashes'])

# Separate features and target
X = data.drop(columns=['Label'])  # Assuming 'Label' is the target column
y = data['Label']

# Normalize the features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Split the data into training and testing sets (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Random Forest Model
rf_model = RandomForestClassifier(random_state=42)
rf_model.fit(X_train, y_train)
rf_predictions = rf_model.predict(X_test)

# Neural Network Model
nn_model = MLPClassifier(max_iter=500, random_state=42)  # Increase the number of iterations

nn_model.fit(X_train, y_train)
nn_predictions = nn_model.predict(X_test)

# Random Forest Accuracy and Classification Report
rf_accuracy = accuracy_score(y_test, rf_predictions)
rf_classification_report = classification_report(y_test, rf_predictions)

# Neural Network Accuracy and Classification Report
nn_accuracy = accuracy_score(y_test, nn_predictions)
nn_classification_report = classification_report(y_test, nn_predictions)

# Output the results
print(f"Random Forest Accuracy: {rf_accuracy}")
print("Random Forest Classification Report:")
print(rf_classification_report)

print(f"Neural Network Accuracy: {nn_accuracy}")
print("Neural Network Classification Report:")
print(nn_classification_report)

# Cross-validation scores for Random Forest
rf_cv_scores = cross_val_score(rf_model, X_scaled, y, cv=5)
print("Random Forest Cross-Validation Scores:", rf_cv_scores)
print("Mean Cross-Validation Accuracy (Random Forest):", rf_cv_scores.mean())

# Cross-validation scores for Neural Network
nn_cv_scores = cross_val_score(nn_model, X_scaled, y, cv=5)
print("Neural Network Cross-Validation Scores:", nn_cv_scores)
print("Mean Cross-Validation Accuracy (Neural Network):", nn_cv_scores.mean())

# Confusion Matrix for both models
rf_conf_matrix = confusion_matrix(y_test, rf_predictions)
nn_conf_matrix = confusion_matrix(y_test, nn_predictions)

print("Random Forest Confusion Matrix:")
print(rf_conf_matrix)

print("Neural Network Confusion Matrix:")
print(nn_conf_matrix)

import joblib

# Save the Random Forest model
joblib.dump(rf_model, 'random_forest_model.pkl')

# Save the Neural Network model
joblib.dump(nn_model, 'neural_network_model.pkl')