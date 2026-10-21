# Task 1.
# Create two NumPy arrays representing the daily step counts of two friends over a week and use element-wise addition, subtraction, multiplication, and division to compare their activity levels.

import numpy as np

friend1 = np.array([5000, 7000, 8000, 6000, 9000, 10000, 7500])
friend2 = np.array([4000, 6500, 7500, 5500, 8500, 9000, 7000])

print("Task 1: Daily Step Counts")
print("Addition:", friend1 + friend2)
print("Subtraction:", friend1 - friend2)
print("Multiplication:", friend1 * friend2)
print("Division:", friend1 / friend2)


# Task 2.
# Simulate a Spotify-like 'Recommended Songs' feature: Given two 3x3 matrices representing user-song interaction scores (user preferences and song popularity), use dot() and matmul() to compute the final recommendation matrix and explain the difference between the two results.

user_preferences = np.array([
    [5, 3, 2],
    [4, 2, 5],
    [3, 5, 4]
])

song_popularity = np.array([
    [1, 2, 3],
    [2, 1, 2],
    [3, 2, 1]
])

dot_result = np.dot(user_preferences, song_popularity)
matmul_result = np.matmul(user_preferences, song_popularity)

print("\nTask 2: Spotify Recommended Songs")
print("Dot Result:\n", dot_result)
print("Matmul Result:\n", matmul_result)
print("Both produce the same result for 2D matrices.")


# Task 3.
# Given a 4x4 NumPy matrix representing the pixel brightness of a small Instagram image, use transpose (T) to rotate the image and then calculate the mean, median, standard deviation, and variance of the pixel values.

image = np.array([
    [10, 20, 30, 40],
    [50, 60, 70, 80],
    [90, 100, 110, 120],
    [130, 140, 150, 160]
])

rotated_image = image.T

print("\nTask 3: Instagram Image")
print("Original Image:\n", image)
print("Transposed Image:\n", rotated_image)
print("Mean:", np.mean(image))
print("Median:", np.median(image))
print("Standard Deviation:", np.std(image))
print("Variance:", np.var(image))


# Task 4.
# Take a 3x3 NumPy matrix representing a Zomato restaurant rating correlation grid and use np.linalg.inv(), np.linalg.det(), and np.linalg.eig() to compute its inverse, determinant, and eigenvalues/eigenvectors. If the matrix is not invertible, modify one value and try again.

correlation_grid = np.array([
    [4, 1, 2],
    [1, 5, 1],
    [2, 1, 6]
], dtype=float)

inverse = np.linalg.inv(correlation_grid)
determinant = np.linalg.det(correlation_grid)
eigenvalues, eigenvectors = np.linalg.eig(correlation_grid)

print("\nTask 4: Zomato Rating Correlation Grid")
print("Inverse:\n", inverse)
print("Determinant:", determinant)
print("Eigenvalues:\n", eigenvalues)
print("Eigenvectors:\n", eigenvectors)


# Task 5.
# Create a NumPy array of shape (2, 6) representing the number of orders placed on Swiggy in two cities over 6 days. Reshape it to (3, 4), flatten it, split it into two equal parts, and then stack both parts vertically.

orders = np.array([
    [100, 120, 130, 110, 140, 150],
    [90, 100, 115, 125, 135, 145]
])

reshaped_orders = orders.reshape(3, 4)
flattened_orders = reshaped_orders.flatten()
part1, part2 = np.split(flattened_orders, 2)
stacked_orders = np.vstack((part1, part2))

print("\nTask 5: Swiggy Orders")
print("Original Array:\n", orders)
print("Reshaped Array:\n", reshaped_orders)
print("Flattened Array:", flattened_orders)
print("First Part:", part1)
print("Second Part:", part2)
print("Vertically Stacked Parts:\n", stacked_orders)
