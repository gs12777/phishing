from sklearn.ensemble import RandomForestClassifier
import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import classification_report, accuracy_score
import numpy as np

# Load the enhanced dataset
data = pd.read_csv('enhanced_dataset.csv')

# Split features and labels
X = data.drop('Label', axis=1)
y = data['Label']

# Split into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Random Forest Classifier with regularization
rf_model = RandomForestClassifier(n_estimators=100, max_depth=10, min_samples_split=5, random_state=42)
rf_model.fit(X_train, y_train)

# Cross-validation score
cv_scores = cross_val_score(rf_model, X, y, cv=5)
print("Cross-Validation Accuracy: {:.2f}%".format(np.mean(cv_scores) * 100))

# Predict and evaluate
y_pred_rf = rf_model.predict(X_test)
print("Random Forest Accuracy:", accuracy_score(y_test, y_pred_rf))
print(classification_report(y_test, y_pred_rf))
