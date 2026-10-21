# Task 1.
# Given a list of delivery timestamps as strings (e.g., ['2024-06-01 14:30', '2024-06-02 09:15', '2024-06-03 20:45']), use pandas and pd.to_datetime() to convert them into datetime objects and print the result.

import pandas as pd
import numpy as np

timestamps = [
    '2024-06-01 14:30',
    '2024-06-02 09:15',
    '2024-06-03 20:45'
]

delivery_times = pd.to_datetime(timestamps)

print("Task 1: Converted Delivery Timestamps")
print(delivery_times)


# Task 2.
# Load a CSV file containing order dates from a Flipkart-style order history (column: 'order_date', format: 'YYYY-MM-DD HH:MM:SS'). Extract the year, month, and weekday for each order and add them as new columns in the DataFrame.

orders = pd.DataFrame({
    'order_date': [
        '2024-06-01 14:30:00',
        '2024-06-02 09:15:00',
        '2024-06-03 20:45:00',
        '2024-06-08 11:00:00',
        '2024-06-09 16:30:00'
    ]
})

orders.to_csv("flipkart_orders.csv", index=False)

df = pd.read_csv("flipkart_orders.csv")
df['order_date'] = pd.to_datetime(df['order_date'])

df['year'] = df['order_date'].dt.year
df['month'] = df['order_date'].dt.month
df['weekday'] = df['order_date'].dt.day_name()

print("\nTask 2: Order Date Details")
print(df)


# Task 3.
# Set the 'order_date' column as the index of your DataFrame and use resampling to calculate the total number of orders placed each week.

df = df.set_index('order_date')

weekly_orders = df.resample('W').size()

print("\nTask 3: Weekly Order Counts")
print(weekly_orders)


# Task 4.
# Suppose you have a DataFrame of Instagram posts with a 'posted_at' column in UTC. Convert these timestamps to 'Asia/Kolkata' timezone and display the first 5 converted times.

instagram_posts = pd.DataFrame({
    'posted_at': [
        '2024-06-01 08:00:00',
        '2024-06-02 10:30:00',
        '2024-06-03 14:15:00',
        '2024-06-04 18:45:00',
        '2024-06-05 21:00:00'
    ]
})

instagram_posts['posted_at'] = pd.to_datetime(
    instagram_posts['posted_at'], utc=True
)

instagram_posts['posted_at'] = instagram_posts['posted_at'].dt.tz_convert(
    'Asia/Kolkata'
)

print("\nTask 4: Instagram Posts in Indian Time")
print(instagram_posts['posted_at'].head())


# Task 5.
# Create a new feature called 'is_weekend' in your DataFrame that marks True if an order was placed on Saturday or Sunday, and False otherwise.

df['is_weekend'] = df.index.dayofweek >= 5

print("\nTask 5: Weekend Order Feature")
print(df[['year', 'month', 'weekday', 'is_weekend']])

