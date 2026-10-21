# Task 1.
# Download a sample CSV file of IPL cricket match scores from Kaggle or any public dataset, and use pd.read_csv() to load it into a DataFrame. Print the first 5 rows to verify the data.

import pandas as pd
import json
import os

ipl_data = pd.read_csv("ipl_matches.csv")

print("Task 1: IPL Cricket Match Scores")
print(ipl_data.head())


# Task 2.
# Find a small JSON dataset of trending songs (for example, from Spotify's API samples or any open JSON file), and use pd.read_json() to import it into a DataFrame. Display the DataFrame's column names and data types using df.info().

songs_data = {
    "song": ["Song A", "Song B", "Song C", "Song D"],
    "artist": ["Artist A", "Artist B", "Artist C", "Artist D"],
    "streams": [150000, 200000, 175000, 300000],
    "rating": [4.5, 4.7, 4.2, 4.9]
}

with open("trending_songs.json", "w") as file:
    json.dump(songs_data, file)

df = pd.read_json("trending_songs.json")

print("\nTask 2: Trending Songs Dataset")
print(df)
df.info()


# Task 3.
# You have a TSV (tab-separated values) file containing Zomato restaurant data. Use pd.read_csv() with the correct separator to load the data, and then use df.describe(include='all') to generate summary statistics.

zomato_data = pd.read_csv("zomato_restaurants.tsv", sep="\t")

print("\nTask 3: Zomato Restaurant Summary")
print(zomato_data.describe(include="all"))


# Task 4.
# Download a large Excel file (at least 10,000 rows) of Flipkart product listings. Use pd.read_excel() with the chunksize parameter to read the file in chunks of 2000 rows, and print the number of rows in each chunk as you iterate.

excel_file = "flipkart_products.xlsx"

print("\nTask 4: Flipkart Product Listings")

chunk_size = 2000

flipkart_data = pd.read_excel(excel_file)

for start in range(0, len(flipkart_data), chunk_size):
    chunk = flipkart_data.iloc[start:start + chunk_size]
    print("Number of rows in chunk:", len(chunk))


# Task 5.
# Use ChatGPT or Copilot to generate a Python code snippet that reads a semicolon-separated CSV of Paytm transactions, detects missing values, and prints out which columns have nulls. Test the code with a small sample file and fix any errors you encounter.

sample_data = {
    "Transaction_ID": [101, 102, 103, 104],
    "Amount": [500, None, 1200, 800],
    "Payment_Mode": ["UPI", "Card", None, "UPI"],
    "Status": ["Success", "Success", "Failed", None]
}

sample_df = pd.DataFrame(sample_data)
sample_df.to_csv("paytm_transactions.csv", sep=";", index=False)

paytm_data = pd.read_csv("paytm_transactions.csv", sep=";")

print("\nTask 5: Paytm Missing Values")
print(paytm_data)

null_counts = paytm_data.isnull().sum()
columns_with_nulls = null_counts[null_counts > 0]

print("\nColumns containing missing values:")
print(columns_with_nulls)
