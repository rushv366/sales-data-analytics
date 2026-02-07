import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

df = pd.read_csv('../data/sales_data_cleaned.csv')

# Aggregate monthly revenue
monthly_sales = df.groupby(df['Date'].dt.to_period('M'))['Revenue'].sum().reset_index()
monthly_sales['Month'] = monthly_sales['Date'].dt.month
monthly_sales['Year'] = monthly_sales['Date'].dt.year

# Prepare data
X = monthly_sales[['Year','Month']]
y = monthly_sales['Revenue']

# Train Linear Regression model
model = LinearRegression()
model.fit(X, y)

# Predict next 3 months
import numpy as np
future_months = pd.DataFrame({'Year':[2026,2026,2026], 'Month':[2,3,4]})
predicted_sales = model.predict(future_months)
print("Next 3 months forecasted revenue:", predicted_sales)
