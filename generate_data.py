import pandas as pd
import random
from datetime import datetime, timedelta

# Products and categories
products = [
    ('T-shirt','Apparel'), ('Jeans','Apparel'), ('Shirt','Apparel'),
    ('Laptop','Electronics'), ('Phone','Electronics'), ('Headphones','Electronics'),
    ('Book','Books'), ('Notebook','Books'), ('Pen','Books')
]

regions = ['North','South','East','West']

# Generate 500 rows
data = []
start_date = datetime(2023,1,1)
for i in range(1,501):
    product, category = random.choice(products)
    quantity = random.randint(1,10)
    price = random.randint(10, 800) if category != 'Books' else random.randint(5,50)
    date = start_date + timedelta(days=random.randint(0,365))
    region = random.choice(regions)
    data.append([1000+i, date.strftime('%Y-%m-%d'), product, category, quantity, price, region])

# Create DataFrame
df = pd.DataFrame(data, columns=['OrderID','Date','Product','Category','Quantity','Price','Region'])

# Save to CSV
df.to_csv('data/sales_data.csv', index=False)
print("500-row sales_data.csv generated successfully!")
