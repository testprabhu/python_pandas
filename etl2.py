import pandas as pd

# Extract
df = pd.read_csv("orders.csv")

# Transformation Logic

# 1. Clean country names (capitalize and fill null)
df['country'] = df['country'].str.title().fillna('Unknown')

# 2. Fill missing amount with 0 and convert to float
df['amount'] = df['amount'].fillna(0.0).astype(float)

# 3. Convert date to datetime format
df['date'] = pd.to_datetime(df['date'])

# 4. Remove duplicates
df = df.drop_duplicates()

# 5. Create derived column: tax = 10% of amount
df['tax'] = df['amount'] * 0.10

# 6. Filter out orders where amount is 0
df = df[df['amount'] > 0]

print(df)
