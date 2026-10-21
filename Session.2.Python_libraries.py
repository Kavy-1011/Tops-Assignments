# Task 1: Create a 2D NumPy array representing the ratings (out of 5) given by 4 users to 5 different food items on Zomato. Use slicing to extract the ratings given by the second and third users only.

import numpy as np

ratings = np.array([
    [4, 5, 3, 4, 2],
    [5, 4, 4, 3, 5],
    [3, 4, 5, 2, 4],
    [4, 3, 4, 5, 3]
])

print("Task 1: Ratings of Second and Third Users")
print(ratings[1:3, :])


# Task 2 : Given a NumPy array of daily steps tracked for 10 days, use boolean indexing to select only the days where the steps were greater than 8000.<br><br><em><strong>Hint:</strong> Use an array like steps = np.array([7500, 8200, 9000, ...]) and apply a boolean condition.</em>

steps = np.array([7500, 8200, 9000, 6500, 10000,
                  7800, 8500, 7200, 9500, 6000])

high_steps = steps[steps > 8000]

print("\nTask 2: Days with More Than 8000 Steps")
print(high_steps)

# Task 3 : Create a NumPy array of IPL team scores for 8 matches. Use fancy indexing to select the scores from matches 2, 5, and 7, and print them.

ipl_scores = np.array([165, 180, 142, 195, 210, 175, 188, 160])

selected_scores = ipl_scores[[1, 4, 6]]

print("\nTask 3: IPL Scores from Matches 2, 5, and 7")
print(selected_scores)

# Task  4 : Suppose you have a NumPy array of product prices from Flipkart. Use broadcasting to apply a 10% discount to all prices and print the new array.<br><br><em><strong>Constraint:</strong> Do not use any loops.</em> 
prices = np.array([1000, 2500, 500, 1200, 3000])

discounted_prices = prices * 0.90

print("\nTask 4: Prices After 10% Discount")
print(discounted_prices)


# Task : 5 Given a NumPy array of user ratings (can be negative, zero, or positive) for songs on Spotify, use boolean masking to set all negative ratings to zero, keeping other ratings unchanged.

song_ratings = np.array([-2, 4, 0, -1, 5, 3, -3, 2])

song_ratings[song_ratings < 0] = 0

print("\nTask 5: Updated Spotify Song Ratings")
print(song_ratings)

