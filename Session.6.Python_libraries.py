# Task 1.
# Download a sample CSV file of IPL player stats (include columns like player name, runs, matches, and some missing values). Load it into a pandas DataFrame and use isnull() and notnull() to print how many missing values are present in each column.

import pandas as pd
import numpy as np

ipl_data = pd.DataFrame({
    "player_name": ["Virat Kohli", "Rohit Sharma", "MS Dhoni", "Jasprit Bumrah", "Hardik Pandya"],
    "runs": [800, 650, np.nan, 250, 400],
    "matches": [15, 14, 12, np.nan, 13]
})

ipl_data.to_csv("ipl_player_stats.csv", index=False)
ipl_data = pd.read_csv("ipl_player_stats.csv")

print("Task 1: IPL Player Stats")
print(ipl_data)

print("\nMissing Values in Each Column:")
print(ipl_data.isnull().sum())

print("\nNon-Missing Values in Each Column:")
print(ipl_data.notnull().sum())


# Task 2.
# Using the loaded IPL player stats DataFrame, apply dropna(axis=0, how='any') to remove all rows with any missing data and display the shape of the DataFrame before and after dropping.

print("\nTask 2: Drop Rows with Missing Values")
print("Shape Before Dropping:", ipl_data.shape)

ipl_cleaned = ipl_data.dropna(axis=0, how="any")

print("Shape After Dropping:", ipl_cleaned.shape)
print(ipl_cleaned)


# Task 3.
# For the 'runs' column in your IPL player stats DataFrame, use fillna() to replace missing values with the mean of the column. Print the updated column to verify the changes.

ipl_data["runs"] = ipl_data["runs"].fillna(ipl_data["runs"].mean())

print("\nTask 3: Runs After Filling Missing Values")
print(ipl_data["runs"])


# Task 4.
# Simulate a Zomato-style restaurant ratings dataset with some missing ratings. Use forward fill (method='ffill') to fill missing values in the ratings column, then use backward fill (method='bfill') for any remaining missing values. Show the before and after results.

restaurant_data = pd.DataFrame({
    "restaurant": ["Restaurant A", "Restaurant B", "Restaurant C", "Restaurant D", "Restaurant E"],
    "rating": [4.5, np.nan, 3.8, np.nan, 4.2]
})

print("\nTask 4: Restaurant Ratings Before Filling")
print(restaurant_data)

restaurant_data["rating"] = restaurant_data["rating"].ffill()
restaurant_data["rating"] = restaurant_data["rating"].bfill()

print("\nRestaurant Ratings After Filling")
print(restaurant_data)


# Task 5.
# Pick any one column with missing values from your dataset and explain which missingness mechanism (MCAR, MAR, or MNAR) is most likely and why, using 2-3 sentences.

print("\nTask 5: Missingness Mechanism")
print("The missing values in the runs column may be MAR (Missing At Random).")
print("For example, missing runs could be related to player-specific factors,")
print("such as incomplete records for players who participated in fewer matches.")
print("This is only a possible explanation; the actual mechanism requires more information.")

