import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score, classification_report
import matplotlib.pyplot as plt
# Load normalized dataset
data_path = r"C:\Users\gurus\project\phishing\normalized_dataset.csv"
data = pd.read_csv(data_path)

# Features and target
X = data.drop(columns=["Label"])  # Replace "Label" if target column is named differently
y = data["Label"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


# Random Forest
rf_model = RandomForestClassifier(random_state=42)
rf_model.fit(X_train, y_train)

rf_predictions = rf_model.predict(X_test)
rf_accuracy = accuracy_score(y_test, rf_predictions)

print("Random Forest Accuracy:", rf_accuracy)

# Cross-validation for Random Forest
rf_cv_scores = cross_val_score(rf_model, X, y, cv=5)
print("Cross-Validation Scores (Random Forest):", rf_cv_scores)
print("Mean Cross-Validation Accuracy (Random Forest):", rf_cv_scores.mean())

# Neural Network
nn_model = MLPClassifier(
    hidden_layer_sizes=(100, 50),  # Two hidden layers
    max_iter=300,
    alpha=0.0001,  # L2 regularization
    random_state=42,
    early_stopping=True,  # Stops when validation score does not improve
    n_iter_no_change=10,  # Patience for early stopping
)
nn_model.fit(X_train, y_train)

nn_predictions = nn_model.predict(X_test)
nn_accuracy = accuracy_score(y_test, nn_predictions)

print("Neural Network Accuracy:", nn_accuracy)

# Cross-validation for Neural Network
nn_cv_scores = cross_val_score(nn_model, X, y, cv=5)
print("Cross-Validation Scores (Neural Network):", nn_cv_scores)
print("Mean Cross-Validation Accuracy (Neural Network):", nn_cv_scores.mean())

# Detailed classification report
print("\nRandom Forest Classification Report:")
print(classification_report(y_test, rf_predictions))

print("\nNeural Network Classification Report:")
print(classification_report(y_test, nn_predictions))

importances = rf_model.feature_importances_
feature_names = X.columns

# Plot
plt.figure(figsize=(10, 6))
plt.barh(feature_names, importances, color="skyblue")
plt.xlabel("Feature Importance")
plt.ylabel("Feature")
plt.title("Random Forest Feature Importance")
plt.show()