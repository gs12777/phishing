import pandas as pd
import matplotlib.pyplot as plt

# Paths to the datasets
data_path = r"C:\Users\gurus\project\phishing\shuffled_dataset.csv"

# Load the dataset
data = pd.read_csv(data_path)

# Check for missing values
print("Missing values in the dataset:")
print(data.isnull().sum())

# Check the range of num_slashes
print("\nSummary of num_slashes:")
print(data['num_slashes'].describe())

# Separate phishing and legitimate URLs
phishing = data[data['Label'] == 1]
legitimate = data[data['Label'] == 0]

# Plot the distribution of num_slashes
plt.figure(figsize=(10, 6))
plt.hist(phishing['num_slashes'], bins=15, alpha=0.7, label='Phishing (1)', color='red')
plt.hist(legitimate['num_slashes'], bins=15, alpha=0.7, label='Legitimate (0)', color='blue')
plt.xlabel('Number of Slashes')
plt.ylabel('Count')
plt.title('Distribution of num_slashes')
plt.legend()
plt.grid(True)
plt.tight_layout()

# Save the plot to an image
plt.savefig(r"C:\Users\gurus\project\phishing\num_slashes_distribution.png")
plt.show()
