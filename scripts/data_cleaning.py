import pandas as pd
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

raw_path = os.path.join(BASE_DIR, "data", "sales_data.csv")
clean_path = os.path.join(BASE_DIR, "data", "sales_data_cleaned.csv")

df = pd.read_csv(raw_path)

df = df.dropna()
df["Date"] = pd.to_datetime(df["Date"])
df["Revenue"] = df["Quantity"] * df["Price"]

df.to_csv(clean_path, index=False)

print("✅ Data cleaned and saved successfully at:")
print(clean_path)
