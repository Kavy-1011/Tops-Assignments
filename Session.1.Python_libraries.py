import numpy as np

# Task 1:
# Install NumPy using pip and import it as np.

# Task 2:
# Create a NumPy array called followers using np.array() that stores the follower counts for 5 Instagram influencers: [1200, 15000, 67000, 340000, 1250000]. Print the array, its shape, number of dimensions, and data type.

followers = np.array([1200, 15000, 67000, 340000, 1250000])

print("Question 2: Instagram Followers")
print("Followers Array:", followers)
print("Shape:", followers.shape)
print("Number of Dimensions:", followers.ndim)
print("Data Type:", followers.dtype)


# Task 3:
# Use np.arange() to generate an array of order IDs for 10 consecutive Zomato orders starting from 101. Print the array and its size.

order_ids = np.arange(101, 111)

print("\nQuestion 3: Zomato Order IDs")
print("Order IDs:", order_ids)
print("Size:", order_ids.size)


# Task 4:
# Create a 3x3 NumPy array using np.eye() to represent a 'like' identity matrix for a new Spotify playlist feature. Print the matrix and explain what the diagonal values represent in a comment.
like_matrix = np.eye(3)

print("\nQuestion 4: Spotify Like Identity Matrix")
print(like_matrix)


# Task 5:
# Convert a Python list of cricket scores [45, 67, 120, 89, 54] to a NumPy array, then use the .itemsize attribute to print how many bytes each score takes in memory.
#Hint: Use np.array() for conversion and .itemsize for memory size.
scores = np.array([45, 67, 120, 89, 54])

print("\nQuestion 5: Cricket Scores")
print("Scores Array:", scores)
print("Bytes per Score:", scores.itemsize)

