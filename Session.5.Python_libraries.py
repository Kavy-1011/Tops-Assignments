# Task 1.
# Connect to a MySQL or PostgreSQL database using SQLAlchemy and pandas, then use pd.read_sql() to load the entire 'restaurants' table (imagine Zomato backend) into a DataFrame and display the first 5 rows.

import pandas as pd
from sqlalchemy import create_engine
from pathlib import Path

engine = create_engine(
    "mysql+pymysql://username:password@localhost:3306/zomato_db"
)

restaurants = pd.read_sql("restaurants", con=engine)

print("Task 1: Restaurants Table")
print(restaurants.head())


# Task 2.
# Use pd.read_sql_query() to fetch only the 'name' and 'rating' columns from a 'movies' table (think BookMyShow-like data) where rating is above 8, and print the resulting DataFrame.

query = "SELECT name, rating FROM movies WHERE rating > 8"

movies = pd.read_sql_query(query, con=engine)

print("\nTask 2: Movies with Rating Above 8")
print(movies)


# Task 3.
# Read a JSON dataset from the URL https://jsonplaceholder.typicode.com/users using pandas, convert it into a DataFrame, and print the usernames column.

url = "https://jsonplaceholder.typicode.com/users"

users_json = pd.read_json(url)

print("\nTask 3: Usernames")
print(users_json["username"])


# Task 4.
# You have two CSV files: 'orders.csv' (order_id, user_id, amount) and 'users.csv' (user_id, username). Load both into DataFrames using pathlib for file paths, then merge them on 'user_id' to show a combined table with username and amount.

orders_path = Path("orders.csv")
users_path = Path("users.csv")

orders = pd.read_csv(orders_path)
users = pd.read_csv(users_path)

merged_data = pd.merge(orders, users, on="user_id")

print("\nTask 4: Merged Orders and Users")
print(merged_data[["order_id", "username", "amount"]])


# Task 5.
# Concatenate two DataFrames representing 'today_orders' and 'yesterday_orders' (each with columns: order_id, item, price), and display the combined DataFrame.
# Constraint: Use pd.concat() and reset the index after concatenation.

today_orders = pd.DataFrame({
    "order_id": [101, 102, 103],
    "item": ["Pizza", "Burger", "Pasta"],
    "price": [250, 150, 220]
})

yesterday_orders = pd.DataFrame({
    "order_id": [98, 99, 100],
    "item": ["Sandwich", "Fries", "Dosa"],
    "price": [120, 90, 100]
})

combined_orders = pd.concat(
    [today_orders, yesterday_orders],
    ignore_index=True
)

print("\nTask 5: Combined Orders")
print(combined_orders)

