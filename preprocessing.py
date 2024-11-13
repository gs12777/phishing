import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
import pickle

# Define the path to the data file
data_path = "C:\\Users\\gurus\\project\\phishing\\url_data.csv"

# Load the collected data
data = pd.read_csv(data_path)

# Display the first few rows of the dataset
print(data.head())

# Prepare data for training
X = data['URL']
y = data['Label'].map({'phishing': 1, 'legitimate': 0})  # Convert labels to binary

# Use TF-IDF Vectorizer to convert URLs to numerical data
vectorizer = TfidfVectorizer(analyzer='char', ngram_range=(3, 5))
X_tfidf = vectorizer.fit_transform(X)

# Split data into training and testing sets (80% training, 20% testing)
X_train, X_test, y_train, y_test = train_test_split(X_tfidf, y, test_size=0.2, random_state=42)

print("Data preprocessing complete. Ready for model training.")

# Initialize the Logistic Regression model
model = LogisticRegression()

# Train the model on the training data
model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = model.predict(X_test)

# Evaluate the model's performance
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy:.2f}")
print("Classification Report:")
print(classification_report(y_test, y_pred))

# Define the paths where the model and vectorizer will be saved
model_path = "C:\\Users\\gurus\\project\\phishing\\phishing_model.pkl"
vectorizer_path = "C:\\Users\\gurus\\project\\phishing\\vectorizer.pkl"

# Save the trained model to a file
with open(model_path, "wb") as model_file:
    pickle.dump(model, model_file)

# Save the vectorizer to a file
with open(vectorizer_path, "wb") as vec_file:
    pickle.dump(vectorizer, vec_file)

print("Model and vectorizer saved successfully.")
