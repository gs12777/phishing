import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler

# Load the enhanced dataset
data = pd.read_csv("enhanced_dataset.csv")

# Split features and labels
X = data.drop(columns=['Label'])  # Dropping the label column, assuming 'Label' column contains phishing/legitimate labels.
y = data['Label']

# Handle URL data: Remove or encode URL features
# We will remove columns that are of type 'object' (likely string or URL type columns)
X_numeric = X.select_dtypes(include=['float64', 'int64'])

# Encode labels
label_encoder = LabelEncoder()
y = label_encoder.fit_transform(y)

# Split into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X_numeric, y, test_size=0.2, random_state=42)

# Scale features (apply StandardScaler to only numerical data)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Save processed data
pd.DataFrame(X_train).to_csv("X_train.csv", index=False)
pd.DataFrame(X_test).to_csv("X_test.csv", index=False)
pd.DataFrame(y_train).to_csv("y_train.csv", index=False)
pd.DataFrame(y_test).to_csv("y_test.csv", index=False)

print("Feature engineering completed. Data saved as X_train.csv, X_test.csv, y_train.csv, and y_test.csv.")
