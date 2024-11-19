import pandas as pd
import matplotlib.pyplot as plt

# Paths to the dataset
data_path = r"C:\Users\gurus\project\phishing\shuffled_dataset.csv"

# Load the dataset
data = pd.read_csv(data_path)

# Separate phishing and legitimate
phishing = data[data['Label'] == 1]
legitimate = data[data['Label'] == 0]

# Plot the distribution of num_slashes
plt.figure(figsize=(10, 6))
plt.hist(phishing['num_slashes'], bins=20, alpha=0.7, label='Phishing (1)', color='red', edgecolor='black')
plt.hist(legitimate['num_slashes'], bins=20, alpha=0.7, label='Legitimate (0)', color='blue', edgecolor='black')

plt.xlabel('Number of Slashes')
plt.ylabel('Count')
plt.title('Distribution of num_slashes')
plt.legend()
plt.grid(True)
plt.tight_layout()

# Save the plot and show it
plt.savefig(r"C:\Users\gurus\project\phishing\num_slashes_distribution.png")
plt.show()
