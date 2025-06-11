import pandas as pd
import os

# Sample data
data = {
    'order_id': [101, 102, 103, 104, 105],
    'country': ['US', 'UK', 'US', 'IN', 'UK'],
    'amount': [250, 180, 300, 120, 200]
}

df = pd.DataFrame(data)

# Create output directory
output_dir = 'partitioned_data'
os.makedirs(output_dir, exist_ok=True)

# Partition by country and save
for country, group in df.groupby('country'):
    file_path = os.path.join(output_dir, f"{country}.csv")
    group.to_csv(file_path, index=False)
    print(f"Saved partition: {file_path}")
