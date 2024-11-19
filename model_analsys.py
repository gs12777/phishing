import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import cross_val_score
import matplotlib.pyplot as plt

# Paths to the datasets
X_train_path = r"C:\Users\gurus\project\phishing\X_train.csv"
X_test_path = r"C:\Users\gurus\project\phishing\X_test.csv"
y_train_path = r"C:\Users\gurus\project\phishing\y_train.csv"
y_test_path = r"C:\Users\gurus\project\phishing\y_test.csv"

# Load the datasets
X_train = pd.read_csv(X_train_path)
X_test = pd.read_csv(X_test_path)
y_train = pd.read_csv(y_train_path).squeeze()
y_test = pd.read_csv(y_test_path).squeeze()

# Random Forest Model
rf_model = RandomForestClassifier(random_state=42)
rf_model.fit(X_train, y_train)
rf_predictions = rf_model.predict(X_test)
rf_accuracy = accuracy_score(y_test, rf_predictions)
print(f"Random Forest Accuracy: {rf_accuracy}")

# Feature Importance
importances = rf_model.feature_importances_
features = X_train.columns
plt.figure(figsize=(10, 6))
plt.barh(features, importances, color='skyblue')
plt.xlabel('Importance')
plt.ylabel('Features')
plt.title('Feature Importance in Random Forest')
plt.tight_layout()
plt.savefig(r"C:\Users\gurus\project\phishing\feature_importance_rf.png")
plt.show()

# Cross-Validation
cv_scores = cross_val_score(rf_model, X_train, y_train, cv=5)
print(f"Cross-Validation Scores: {cv_scores}")
print(f"Mean Cross-Validation Accuracy: {cv_scores.mean()}")
