"""
NumPy Practice Log
Topics: Arrays, Indexing, Reshaping, Broadcasting, Matrix Ops, Stats

"""

import numpy as np

print("=== NumPy Practice Log ===\n")

# ---------------------------------------------------------
# 1. CREATING ARRAYS
# ---------------------------------------------------------
print("--- 1. Creating Arrays ---")

# 1D Array
arr1 = np.array([10, 20, 30, 40, 50])
print(f"1D Array: {arr1}")
# Expected Output: 1D Array: [10 20 30 40 50]

# 2D Array (Matrix)
arr2 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(f"2D Array:\n{arr2}")
# Expected Output:
# 2D Array:
# [[1 2 3]
#  [4 5 6]
#  [7 8 9]]

# Array of Zeros and Ones
zeros = np.zeros((3, 3))
ones = np.ones((2, 4))
print(f"\nZeros (3x3):\n{zeros}")
# Expected Output: 3x3 matrix of 0.0
print(f"Ones (2x4):\n{ones}")
# Expected Output: 2x4 matrix of 1.0

# ---------------------------------------------------------
# 2. BASIC OPERATIONS (Vectorization)
# ---------------------------------------------------------
print("\n--- 2. Basic Operations ---")

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print(f"a: {a}")
print(f"b: {b}")
# Expected Output: a: [1 2 3] / b: [4 5 6]

print(f"Add (a + b): {a + b}")
# Expected Output: Add (a + b): [5 7 9]

print(f"Subtract (a - b): {a - b}")
# Expected Output: Subtract (a - b): [-3 -3 -3]

print(f"Multiply (a * b): {a * b}")
# Expected Output: Multiply (a * b): [4 10 18] (Element-wise multiplication)

print(f"Divide (a / 2): {a / 2}")
# Expected Output: Divide (a / 2): [0.5 1.  1.5]

# ---------------------------------------------------------
# 3. INDEXING & SLICING
# ---------------------------------------------------------
print("\n--- 3. Indexing & Slicing ---")

data = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
print(f"Full Array: {data}")
# Expected Output: Full Array: [ 10  20  30  40  50  60  70  80  90 100]

print(f"First element (index 0): {data[0]}")
# Expected Output: First element (index 0): 10

print(f"Last element (index -1): {data[-1]}")
# Expected Output: Last element (index -1): 100

print(f"Slicing [2:5] (indices 2,3,4): {data[2:5]}")
# Expected Output: Slicing [2:5] (indices 2,3,4): [30 40 50]

print(f"Reverse array: {data[::-1]}")
#  Output: Reverse array: [100  90  80  70  60  50  40  30  20  10]

print(f"Every 2nd element: {data[::2]}")
#  Output: Every 2nd element: [ 10  30  50  70  90]

# ---------------------------------------------------------
# 4. RESHAPING & BROADCASTING
# ---------------------------------------------------------
print("\n--- 4. Reshaping & Broadcasting ---")

# Reshape 1D to 2D
flat = np.arange(12) # 0 to 11
print(f"Original (1D, 12 elements): {flat}")
#  Output: Original (1D, 12 elements): [ 0  1  2  3  4  5  6  7  8  9 10 11]

reshaped = flat.reshape(3, 4)
print(f"Reshaped to (3x4):\n{reshaped}")
#  Output:
# Reshaped to (3x4):
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]]

# Broadcasting (Adding a scalar to a matrix)
print("\nAdding 10 to every element in reshaped array:")
broadcasted = reshaped + 10
print(broadcasted)
#  Output:
# [[10 11 12 13]
#  [14 15 16 17]
#  [18 19 20 21]]

# ---------------------------------------------------------
# 5. MATRIX OPERATIONS (Dot Product & Transpose)
# ---------------------------------------------------------
print("\n--- 5. Matrix Operations ---")

mat_a = np.array([[1, 2], [3, 4]])
mat_b = np.array([[5, 6], [7, 8]])

print(f"Matrix A:\n{mat_a}")
print(f"Matrix B:\n{mat_b}")
#  Output:
# Matrix A:
# [[1 2]
#  [3 4]]
# Matrix B:
# [[5 6]
#  [7 8]]

# Transpose
print(f"Transpose of A:\n{mat_a.T}")
#  Output:
# Transpose of A:
# [[1 3]
#  [2 4]]

# Dot Product (Matrix Multiplication)
dot_result = np.dot(mat_a, mat_b)
print(f"Dot Product (A . B):\n{dot_result}")
#  Output:
# Dot Product (A . B):
# [[19 22]
#  [43 50]]

# ---------------------------------------------------------
# 6. STATISTICAL FUNCTIONS
# ---------------------------------------------------------
print("\n--- 6. Statistical Functions ---")

scores = np.array([85, 92, 78, 90, 88, 76, 95, 82])
print(f"Scores: {scores}")
#  Output: Scores: [85 92 78 90 88 76 95 82]

print(f"Mean: {np.mean(scores):.2f}")
#  Output: Mean: 85.75

print(f"Median: {np.median(scores)}")
#  Output: Median: 87.0

print(f"Standard Deviation: {np.std(scores):.2f}")
#  Output: Standard Deviation: 6.36 (approx)

print(f"Min: {np.min(scores)}, Max: {np.max(scores)}")
#  Output: Min: 76, Max: 95

print(f"Sum: {np.sum(scores)}")
#  Output: Sum: 686

print(f"Argmax (index of highest): {np.argmax(scores)}")
#  Output: Argmax (index of highest): 6 (Index of 95)

# ---------------------------------------------------------
# 7. CONDITIONAL OPERATIONS (Masking)
# ---------------------------------------------------------
print("\n--- 7. Conditional Operations (Masking) ---")

# Find all scores greater than 85
high_scores = scores[scores > 85]
print(f"Scores > 85: {high_scores}")
# Output: Scores > 85: [92 90 88 95]

# Replace all scores < 80 with 80 (Passing grade)
scores_fixed = np.where(scores < 80, 80, scores)
print(f"Scores after fixing (<80 -> 80): {scores_fixed}")
# Output: Scores after fixing (<80 -> 80): [85 92 80 90 88 80 95 82]

