import matplotlib.pyplot as plt
import pandas as pd

# Load the dataset
data_path = r"C:\Users\gurus\project\phishing\shuffled_dataset.csv"
data = pd.read_csv(data_path)

# Check value counts for num_slashes
num_slashes_counts = data['num_slashes'].value_counts()

# Plot the bar chart
plt.figure(figsize=(10, 6))
num_slashes_counts.plot(kind='bar', color='skyblue', edgecolor='black')

plt.xlabel('Number of Slashes')
plt.ylabel('Count')
plt.title('Bar Plot of num_slashes')
plt.tight_layout()

# Save the plot and show it
plt.savefig(r"C:\Users\gurus\project\phishing\num_slashes_bar_plot.png")
plt.show()
