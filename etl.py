import pandas as pd
from sqlalchemy import create_engine
import datetime

# ---------------------
# Step 1: Extract
# ---------------------
csv_file = "sales_data.csv"
df = pd.read_csv(csv_file)
print(df.head())  # Display first few rows for verification

# ---------------------
# Step 2: Transform
# ---------------------
# - Standardize country names (capitalize)
# - Handle NULL purchase amounts
# - Convert purchase_date to datetime
# - Add a "processed_date" column

df['country'] = df['country'].str.title()
df['purchase_amount'] = df['purchase_amount'].fillna(0.0)
df['purchase_date'] = pd.to_datetime(df['purchase_date'])
df['processed_date'] = datetime.datetime.now()

# ---------------------
# Step 3: Load
# ---------------------
# PostgreSQL connection: postgresql+psycopg2://user:password@host:port/database
engine = create_engine("postgresql+psycopg2://postgres:test123@localhost:5432/salesdb")

# Load into 'customer_sales' table
df.to_sql('customer_sales', engine, if_exists='replace', index=False)

print("✅ ETL data migration complete!")
