import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, confusion_matrix
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras.regularizers import l2

# 1. Load the datasets
X_train = pd.read_csv('X_train.csv')  # Update with the correct path
X_test = pd.read_csv('X_test.csv')    # Update with the correct path
y_train = pd.read_csv('y_train.csv')  # Update with the correct path
y_test = pd.read_csv('y_test.csv')    # Update with the correct path

print(f"Training Set Size: {X_train.shape}")
print(f"Testing Set Size: {X_test.shape}")

# 2. Machine Learning Models (Random Forest and SVM)

# --- Random Forest ---
rf_model = RandomForestClassifier(n_estimators=100, max_depth=10, min_samples_split=4, min_samples_leaf=2, random_state=42)
rf_model.fit(X_train, y_train)
rf_predictions = rf_model.predict(X_test)
rf_accuracy = accuracy_score(y_test, rf_predictions)

# --- Support Vector Machine ---
svm_model = SVC(kernel='linear', random_state=42)
svm_model.fit(X_train, y_train)
svm_predictions = svm_model.predict(X_test)
svm_accuracy = accuracy_score(y_test, svm_predictions)

# 3. Print Accuracy Results
print(f"Random Forest Accuracy: {rf_accuracy:.4f}")
print(f"SVM Accuracy: {svm_accuracy:.4f}")

# 4. Confusion Matrices for Machine Learning Models

# Random Forest Confusion Matrix
cf_matrix_rf = confusion_matrix(y_test, rf_predictions)
sns.heatmap(cf_matrix_rf, annot=True, fmt="d", cmap="Blues", xticklabels=["Legitimate", "Phishing"], yticklabels=["Legitimate", "Phishing"])
plt.title("Confusion Matrix - Random Forest")
plt.savefig('rf_confusion_matrix.png')
plt.clf()

# SVM Confusion Matrix
cf_matrix_svm = confusion_matrix(y_test, svm_predictions)
sns.heatmap(cf_matrix_svm, annot=True, fmt="d", cmap="Blues", xticklabels=["Legitimate", "Phishing"], yticklabels=["Legitimate", "Phishing"])
plt.title("Confusion Matrix - SVM")
plt.savefig('svm_confusion_matrix.png')
plt.clf()

# 5. Deep Learning Model (Neural Network)

# Neural Network Model
nn_model = Sequential()
nn_model.add(Dense(64, input_dim=X_train.shape[1], activation='relu', kernel_regularizer=l2(0.01)))
nn_model.add(Dropout(0.5))  # 50% Dropout rate
nn_model.add(Dense(32, activation='relu'))
nn_model.add(Dense(1, activation='sigmoid'))  # Binary classification

nn_model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
history_nn = nn_model.fit(X_train, y_train, epochs=20, batch_size=32, validation_split=0.2)

# Evaluate Neural Network
nn_accuracy = nn_model.evaluate(X_test, y_test)
print(f"Neural Network Accuracy: {nn_accuracy[1]:.4f}")

# Plot Neural Network Accuracy
plt.plot(history_nn.history['accuracy'], label='Train Accuracy')
plt.plot(history_nn.history['val_accuracy'], label='Validation Accuracy')
plt.title('Neural Network Accuracy')
plt.xlabel('Epochs')
plt.ylabel('Accuracy')
plt.legend()
plt.savefig('nn_accuracy.png')
plt.clf()

# 6. Save Accuracy Results to Text File
with open('model_accuracies.txt', 'w') as f:
    f.write(f"Random Forest Accuracy: {rf_accuracy:.4f}\n")
    f.write(f"SVM Accuracy: {svm_accuracy:.4f}\n")
    f.write(f"Neural Network Accuracy: {nn_accuracy[1]:.4f}\n")

# Final Output
print("Model development completed. Results saved in the following files:")
print("1. Confusion Matrices for Random Forest and SVM: rf_confusion_matrix.png, svm_confusion_matrix.png")
print("2. Neural Network Accuracy Plot: nn_accuracy.png")
print("3. Model Accuracy Results: model_accuracies.txt")
