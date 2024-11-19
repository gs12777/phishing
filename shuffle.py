import pandas as pd

# Load the enhanced dataset
data = pd.read_csv("enhanced_dataset.csv")  # Replace with your actual file path

# Shuffle the dataset
data = data.sample(frac=1, random_state=42).reset_index(drop=True)

# Save the shuffled dataset
data.to_csv("shuffled_dataset.csv", index=False)

print("Dataset shuffled and saved as 'shuffled_dataset.csv'.")
