# Task 1.
# Download a small sample of your recent Zomato order history as a CSV (or create a mock CSV with restaurant names and order dates), then use pandas' duplicated() function to find and print any duplicate orders based on restaurant name and date.

import pandas as pd

zomato_data = pd.DataFrame({
    "restaurant_name": ["Dominos", "McDonalds", "Dominos", "KFC", "McDonalds"],
    "order_date": ["2026-10-10", "2026-10-11", "2026-10-10", "2026-10-12", "2026-10-11"]
})

zomato_data.to_csv("zomato_orders.csv", index=False)
zomato_data = pd.read_csv("zomato_orders.csv")

duplicates = zomato_data.duplicated(
    subset=["restaurant_name", "order_date"],
    keep=False
)

print("Task 1: Duplicate Orders")
print(zomato_data[duplicates])


# Task 2.
# Given a list of Flipkart product reviews with some duplicate entries, use value_counts() in pandas to identify which review texts are repeated most often and display the top 3 most common duplicate reviews.

reviews = pd.Series([
    "Good product",
    "Excellent quality",
    "Good product",
    "Worth the price",
    "Good product",
    "Excellent quality",
    "Average product",
    "Excellent quality",
    "Nice product"
])

review_counts = reviews.value_counts()
duplicate_reviews = review_counts[review_counts > 1].head(3)

print("\nTask 2: Top 3 Most Common Duplicate Reviews")
print(duplicate_reviews)


# Task 3.
# Create a DataFrame with mock data for Spotify playlists, including playlist names and creator usernames, where some rows are exact duplicates. Use drop_duplicates() to remove duplicate playlists and print the cleaned DataFrame.

playlists = pd.DataFrame({
    "playlist_name": ["Chill Vibes", "Workout Hits", "Chill Vibes", "Top Hits", "Workout Hits"],
    "creator_username": ["user1", "user2", "user1", "user3", "user2"]
})

cleaned_playlists = playlists.drop_duplicates()

print("\nTask 3: Cleaned Spotify Playlists")
print(cleaned_playlists)


# Task 4.
# Suppose you have a DataFrame of Instagram usernames where some entries have typos (like 'insta_queen', 'insta-queen', 'instaqueen'). Use the replace() function to standardize all these variants to 'instaqueen'.

instagram_data = pd.DataFrame({
    "username": ["insta_queen", "insta-queen", "instaqueen", "user123", "insta_queen"]
})

instagram_data["username"] = instagram_data["username"].replace({
    "insta_queen": "instaqueen",
    "insta-queen": "instaqueen"
})

print("\nTask 4: Standardized Instagram Usernames")
print(instagram_data)


# Task 5.
# You have a DataFrame column for payment status from a Paytm-like app with mixed values: 'Yes', 'yes', 'Y', 'No', 'no', 'N', and some with extra spaces. Write code to unify this column so all paid statuses become 1 and all unpaid statuses become 0, trimming whitespace and fixing capitalization where needed.

paytm_data = pd.DataFrame({
    "payment_status": ["Yes", "yes", "Y", "No", "no", "N", " Yes ", "  n  "]
})

paytm_data["payment_status"] = (
    paytm_data["payment_status"]
    .str.strip()
    .str.lower()
    .map({"yes": 1, "y": 1, "no": 0, "n": 0})
)

print("\nTask 5: Standardized Paytm Payment Status")
print(paytm_data)

