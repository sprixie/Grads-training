import numpy as np
import pandas as pd

# Set random seed for reproducibility
np.random.seed(42)

# Parameters for the dataset
num_rows = 1000000  # 1 million rows
num_categories = 5   # Number of categories for grouping

# Create a sample dataset
ids = np.arange(num_rows)
categories = np.random.choice([f'Category {i}' for i in range(num_categories)], num_rows)
values = np.random.rand(num_rows)

# Introduce duplicates by repeating some of the entries
duplicates = np.random.choice(ids, size=num_rows // 10)  # Duplicate 10% of the IDs
ids = np.concatenate([ids, duplicates])
categories = np.concatenate([categories, categories[duplicates]])
values = np.concatenate([values, values[duplicates]])

# Introduce some missing values (10% NaN)
missing_indices = np.random.choice(len(ids), size=int(len(ids) * 0.1), replace=False)
values[missing_indices] = np.nan  # Set 10% of 'value' to NaN

# Shuffle the dataset
indices = np.arange(len(ids))
np.random.shuffle(indices)

# Create the final DataFrame
final_data = pd.DataFrame({
    'id': ids[indices],
    'category': categories[indices],
    'value': values[indices]
})

# Save to CSV
final_data.to_csv('large_dataset.csv', index=False)

print("Dataset created and saved as 'large_dataset.csv'")

