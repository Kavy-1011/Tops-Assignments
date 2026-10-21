# Task 1.
# Given a CSV file containing Zomato restaurant ratings, use pandas to detect outliers in the 'user_rating' column using the IQR method and print the indices of the detected outliers.


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

zomato_data = pd.DataFrame({
    "restaurant": ["A", "B", "C", "D", "E", "F", "G"],
    "user_rating": [3.5, 4.0, 4.2, 3.8, 4.1, 4.0, 1.0]
})

zomato_data.to_csv("zomato_ratings.csv", index=False)
zomato_data = pd.read_csv("zomato_ratings.csv")

Q1 = zomato_data["user_rating"].quantile(0.25)
Q3 = zomato_data["user_rating"].quantile(0.75)
IQR = Q3 - Q1

lower_limit = Q1 - 1.5 * IQR
upper_limit = Q3 + 1.5 * IQR

outliers = zomato_data[
    (zomato_data["user_rating"] < lower_limit) |
    (zomato_data["user_rating"] > upper_limit)
]

print("Task 1: Outlier Indices")
print(outliers.index.tolist())


# Task 2.
# Create a boxplot for the 'order_amount' column from a Swiggy orders dataset using matplotlib, and visually identify any outliers present.

swiggy_data = pd.DataFrame({
    "order_amount": [150, 200, 250, 180, 300, 220, 275, 5000]
})

plt.boxplot(swiggy_data["order_amount"])
plt.title("Swiggy Order Amount Outliers")
plt.ylabel("Order Amount")
plt.xlabel("Swiggy Orders")
plt.show()


# Task 3.
# Apply winsorization to the 'transaction_amount' column in a Paytm transactions DataFrame to cap all values above the 95th percentile and below the 5th percentile, then display the updated column statistics.

paytm_data = pd.DataFrame({
    "transaction_amount": [100, 250, 300, 450, 500, 700, 900, 1200, 1500, 5000]
})

lower_cap = paytm_data["transaction_amount"].quantile(0.05)
upper_cap = paytm_data["transaction_amount"].quantile(0.95)

paytm_data["transaction_amount"] = paytm_data["transaction_amount"].clip(
    lower=lower_cap,
    upper=upper_cap
)

print("\nTask 3: Winsorized Transaction Statistics")
print(paytm_data["transaction_amount"].describe())


# Task 4.
# You have a DataFrame of Flipkart product prices stored as strings with currency symbols (e.g., '₹1,299'). Convert this column to numeric type using pandas, ensuring all non-numeric characters are removed.

flipkart_data = pd.DataFrame({
    "product": ["Phone", "Headphones", "Laptop", "Mouse"],
    "price": ["₹1,299", "₹999", "₹45,999", "₹499"]
})

flipkart_data["price"] = (
    flipkart_data["price"]
    .str.replace(r"[^0-9.]", "", regex=True)
    .astype(float)
)

print("\nTask 4: Numeric Product Prices")
print(flipkart_data)
print(flipkart_data.dtypes)


# Task 5.
# Fix the following code snippet where the 'is_premium' column in a Spotify user DataFrame is a mix of boolean, string, and integer types. Convert the entire column to boolean type, treating 'True', 1, and 'yes' as True, and everything else as False.

spotify_data = pd.DataFrame({
    "username": ["User1", "User2", "User3", "User4", "User5", "User6"],
    "is_premium": [True, "True", 1, "yes", "False", 0]
})

spotify_data["is_premium"] = spotify_data["is_premium"].apply(
    lambda x: (
        x is True or
        (isinstance(x, (int, np.integer)) and not isinstance(x, bool) and x == 1) or
        (isinstance(x, str) and x.strip().lower() == "yes") or
        (isinstance(x, str) and x.strip().lower() == "true")
    )
)

print("\nTask 5: Spotify Premium Users")
print(spotify_data)
print(spotify_data.dtypes)

