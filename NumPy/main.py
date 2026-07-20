import numpy as np

# =================================================================================================================
#                                         WHAT IS NUMPY?
# =================================================================================================================
# NumPy (Numerical Python) is the fundamental package for scientific computing in Python.
# It provides:
# 1. A powerful N-dimensional array object (ndarray).
# 2. Sophisticated (broadcasting) functions.
# 3. Tools for integrating C/C++ and Fortran code.
# 4. Useful linear algebra, Fourier transform, and random number capabilities.
#
# Why use NumPy?
# - Speed: NumPy arrays are faster than Python lists because they are stored in contiguous blocks of memory.
# - Functionality: Optimized mathematical operations on arrays.

# print the numpy version
print("Numpy version: ", np.__version__)

#                                         create a numpy array 
#                                      Scalar Arithmetic Operations
# np.array() creates a NumPy array. Unlike Python lists, NumPy arrays are:
# 1. Homogeneous: All elements are of the same data type.
# 2. Fixed Size: Size is determined at creation.
arr = np.array([1, 2, 3, 4, 5])
print("Numpy array: ", arr)
 # multiply the array by 2
# VECTORIZATION:
# Operations in NumPy are "vectorized". This means you can operate on the entire array 
# at once without writing an explicit loop (like `for x in arr:`). 
# This leverages low-level C optimizations for speed.
# BROADCASTING:
# When you do `arr * 2`, NumPy "broadcasts" the scalar `2` across the entire array `arr`.
print("Numpy array multiplied by 2: ", arr * 2)
 # add the array to itself
print("Numpy array added to itself: ", arr + arr)
 # subtract the array from itself
print("Numpy array subtracted from itself: ", arr - arr)
 # divide the array by itself
print("Numpy array divided by itself: ", arr / arr)
 # multiply the array by itself
print("Numpy array multiplied by itself: ", arr * arr)
 # divide the array by itself
print("Numpy array divided by itself: ", arr / arr)
 # power the array 
print("Numpy array powered by itself: ", arr ** 3)


arr = np.array([1, 2, 3])

new_arr = np.append(arr, 4)

print(new_arr)
# [1 2 3 4]

#--------------------------------------------------------------------------------------------------
# Print the type 
print("Numpy array type: ", type(arr))

# create a two dimensional numpy array
arr2 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("Two dimensional numpy array: ", arr2)

# print the shape of the array
print("Two dimensional numpy array shape: ", arr2.shape)
# print the number of dimensions of the array
print("Two dimensional numpy array number of dimensions: ", arr2.ndim)

# print the array
print("Two dimensional numpy array: ", arr2)


# access the element in the second row and third column
print("Element in the second row and third column: ", arr2[1, 2]) # arr2[1][2]

#                           create a 3D numpy array with shape (3, 3, 2) and print the shape and number of dimensions
word_3dMatrix = np.array([[['Hello', 'World'], ['Hello', 'World'], ['Hello', 'World']], [['Hello', 'World'], ['Hello', 'World'], ['Hello', 'World']], [['Hello', 'World'], ['Hello', 'World'], ['Hello', 'World']]])
print("3D numpy array: ", word_3dMatrix)
print("3D numpy array shape: ", word_3dMatrix.shape)
print("3D numpy array number of dimensions: ", word_3dMatrix.ndim)
word = word_3dMatrix[0, 0, 0] + " " + word_3dMatrix[0, 0, 1]
print("Word: ", word)


# --------------------------------------------------------------
#                                                                   row                 column
#                                            SLICING ARRAYS arr[start:stop:step , start:stop:step]
# CRITICAL CONCEPT: VIEWS VS COPIES
# Slicing a NumPy array returns a VIEW of the original array, not a copy.
# This means if you modify the slice, you modify the original array!
# To get a copy, you must explicitly use .copy().

# Create a 2D NumPy array (matrix)
arr = np.array([
    [1,  2,  3,  4],
    [5,  6,  7,  8],
    [9, 10, 11, 12]
])

# The array looks like this:
# [
#   [ 1,  2,  3,  4],
#   [ 5,  6,  7,  8],
#   [ 9, 10, 11, 12]
# ]

# --------------------------------------------------
# SLICING ROWS
# --------------------------------------------------

# Get the first row (row index 0)
row_0 = arr[0]
# Result: [1 2 3 4]

# Get the first two rows (rows from index 0 to 2, 2 is NOT included)
rows_0_1 = arr[0:2]
# Result:
# [
#   [1 2 3 4],
#   [5 6 7 8]
# ]

# Get all rows starting from row index 1
rows_from_1 = arr[1:]
# Result:
# [
#   [5 6 7 8],
#   [9 10 11 12]
# ]

# --------------------------------------------------
# SLICING COLUMNS
# --------------------------------------------------

# Get all rows, column at index 0 (first column)
col_0 = arr[:, 0]
# Result: [1 5 9]

# Get all rows, columns from index 1 to 3 (3 not included)
cols_1_2 = arr[:, 1:3]
# Result:
# [
#   [ 2  3],
#   [ 6  7],
#   [10 11]
# ]

# Get all rows, last column
last_col = arr[:, -1]
# Result: [4 8 12]

# --------------------------------------------------
# SLICING ROWS AND COLUMNS TOGETHER
# --------------------------------------------------

# Get rows 0 to 2 and columns 1 to 3
sub_matrix = arr[0:2, 1:3]
# Result:
# [
#   [2 3],
#   [6 7]
# ]

# Get the middle element (row 1, column 2)
single_value = arr[1, 2]
# Result: 7

# --------------------------------------------------
# STEP IN SLICING
# --------------------------------------------------

# Get every second column
every_second_col = arr[:, ::2]
# Result:
# [
#   [ 1  3],
#   [ 5  7],
#   [ 9 11]
# ]



#--------------------------------------------------------------------------------------------------
#                                          Array Manipulation & UFuncs
#--------------------------------------------------------------------------------------------------
# Universal Functions (ufuncs):
# These are mathematical functions that operate element-by-element on ndarrays.
# They are implemented in C and are very fast.


# create a 2D array
arr = np.array([90, 2.5, 30])
print(" print square root of the array: ", np.sqrt(arr))
print(" print the rounded array: ", np.round(arr)) # round to the nearest integer
print(" print the floor array: ", np.floor(arr)) # round down to the nearest integer
print(" print the ceil array: ", np.ceil(arr)) # round up to the nearest integer
print(" print the square of the array: ", np.square(arr)) 
# print(" print cube of the array: ", np.cube(arr))
print(" print absolute of the array: ", np.abs(arr))
print(" print sine of the array: ", np.sin(arr))
print(" print cosine of the array: ", np.cos(arr))
print(" print tangent of the array: ", np.tan(arr))
print(" print exponential of the array: ", np.exp(arr))
print(" print log of the array: ", np.log(arr)) 


# =================================================================================================================
#                           GUIDE: COMPARISON OPERATIONS IN PYTHON & NUMPY
# =================================================================================================================

# ------------------------------------------------------------------------------
# PART 1: STANDARD PYTHON COMPARISONS (SCALARS)
# ------------------------------------------------------------------------------
# In standard Python, comparison operators return a single Boolean value (True/False).
# These are the standard operators:
# >   Greater than
# <   Less than
# >=  Greater than or equal to
# <=  Less than or equal to
# ==  Equal to
# !=  Not equal to

x = 10
y = 5

# Examples: 
print(f"comparing between two numbers {x} , {y}")
print(f"is {x} > {y} -> " , x > y)   # True
print(f"is {x} == 10 -> ",x == 10) # True
print(f"is {x} != {y} -> " , x != y)  # True

# ------------------------------------------------------------------------------
# PART 2: NUMPY ELEMENT-WISE COMPARISONS
# ------------------------------------------------------------------------------
# NumPy takes these standard operators and "vectorizes" them.
# Instead of returning a single True/False, it performs the comparison on
# EVERY element of the array and returns a new Boolean array.

arr = np.array([10, 20, 30, 40, 50])

# Check which elements are greater than 25
result = arr > 25
# Explanation: NumPy checks 10>25, 20>25, 30>25, etc.
# Result: [False, False, True, True, True]
print(result , f"this is the result of if {arr} elements > 25")
# Check equality
# Result: [False, False, True, False, False]
equality_check = (arr == 30) 

# ------------------------------------------------------------------------------
# PART 3: COMPARISON BETWEEN TWO ARRAYS
# ------------------------------------------------------------------------------
# If you compare two arrays of the same shape, NumPy compares them position by position.

a = np.array([1, 2, 3, 4])
b = np.array([4, 2, 2, 4])

# Compare a and b
# 1 vs 4 (False), 2 vs 2 (True), 3 vs 2 (False), 4 vs 4 (True)
# Result: [False, True, False, True]
comparison = (a == b)
print(comparison , f"this is the result of if {a} == {b} or not .")

import numpy as np

# ----------------------------------------------------------------------------

# Sample arrays
arr = np.array([10, 15, 25, 40, 50])
data = np.array([5, 12, 67, 2, 45])

# ----------------------------------------------------------------------------
# Use & | ~ instead of and or
# Parentheses are REQUIRED

complex_filter = (arr > 20) & (arr < 45)
filtered_arr = arr[complex_filter]

print("BITWISE LOGIC (20 < x < 45):")
print(filtered_arr)
print("-" * 40)

# ----------------------------------------------------------------------------
# BOOLEAN MASKING (FILTERING DATA)
# ----------------------------------------------------------------------------
subset = data[data > 10]

print("BOOLEAN MASKING (data > 10):")
print(subset)
print("-" * 40)

# ----------------------------------------------------------------------------
# AGGREGATE BOOLEAN CHECKS (ANY / ALL)
# ----------------------------------------------------------------------------
bools = np.array([True, False, True])

has_any_true = np.any(bools)
are_all_true = np.all(bools)
is_arr_positive = np.all(arr > 0)

print("AGGREGATE BOOLEANS:")
print("Any True in bools?", has_any_true)
print("All True in bools?", are_all_true)
print("All values in arr positive?", is_arr_positive)
print("-" * 40)

# ----------------------------------------------------------------------------
# AFE FLOAT COMPARISONS
# ----------------------------------------------------------------------------
f1 = 0.1 + 0.2
f2 = 0.3

safe_compare = np.isclose(f1, f2)

print("FLOAT COMPARISON (SAFE CHECK):")
print("0.1 + 0.2 ≈ 0.3 ?", safe_compare)
print("-" * 40)


#----------------------------------------------------------------------------
#----------------------------------------------------------------------------
#----------------------------------------------------------------------------
#----------------------------------------------------------------------------



# =================================================================================================================
#                                       Matrix Multiplication 
# =================================================================================================================

# Matrix A: shape (3, 3)
matrix1 = np.array([
    [1, 2, 3],
    [1, 2, 3],
    [1, 2, 3]
])

# Matrix B: shape (3, 1)
matrix2 = np.array([
    [0],
    [0],
    [0]
])

# Shapes (conditions check)
print("matrix1 shape:", matrix1.shape)  # (3, 3)
print("matrix2 shape:", matrix2.shape)  # (3, 1)

# Matrix multiplication (valid because 3 == 3)
# Rule for Matrix Multiplication (A @ B):
# If A is (m, n) and B is (n, p), result is (m, p).
# The inner dimensions (n) must match.
result = matrix1 @ matrix2

print("Result shape:", result.shape)    # (3, 1)
print("Result:")
print(result)







# =================================================================================================================
#                                       Aggregate Functions  
# =================================================================================================================

# Create a NumPy 2D array
arr = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

# ---------------------------------
# sum(): calculates the total sum
# ---------------------------------

np.sum(arr)
# Adds all elements in the array
# 1 + 2 + 3 + 4 + 5 + 6 = 21

np.sum(arr, axis=0)
# Adds elements column-wise
# Column 0: 1 + 4 = 5
# Column 1: 2 + 5 = 7
# Column 2: 3 + 6 = 9

np.sum(arr, axis=1)
# Adds elements row-wise
# Row 0: 1 + 2 + 3 = 6
# Row 1: 4 + 5 + 6 = 15

# Understanding AXIS:
# axis=0: "Combine the rows". The operation runs vertically down the columns.
#         (Result size matches number of columns)
# axis=1: "Combine the columns". The operation runs horizontally across the rows.
#         (Result size matches number of rows)

# ---------------------------------
# mean(): calculates the average
# ---------------------------------

np.mean(arr)
# Computes the average of all elements

np.mean(arr, axis=0)
# Average of each column

np.mean(arr, axis=1)
# Average of each row


# ---------------------------------
# max(): finds the maximum value
# ---------------------------------

np.max(arr)
# Returns the largest value in the entire array

np.max(arr, axis=0)
# Maximum value in each column

np.max(arr, axis=1)
# Maximum value in each row


# ---------------------------------
# min(): finds the minimum value
# ---------------------------------

np.min(arr)
# Returns the smallest value in the entire array

np.min(arr, axis=0)
# Minimum value in each column

np.min(arr, axis=1)
# Minimum value in each row


# ---------------------------------
# std(): standard deviation
# Measures how spread out the values are
# ---------------------------------

np.std(arr)
# Standard deviation of all elements

np.std(arr, axis=0)
# Standard deviation of each column

np.std(arr, axis=1)
# Standard deviation of each row


# ---------------------------------
# var(): variance
# Square of the standard deviation
# ---------------------------------

np.var(arr)
# Variance of all elements

np.var(arr, axis=0)
# Variance of each column

np.var(arr, axis=1)
# Variance of each row


# ---------------------------------
# prod(): product of elements
# ---------------------------------

np.prod(arr)
# Multiplies all elements together

np.prod(arr, axis=0)
# Product of each column

np.prod(arr, axis=1)
# Product of each row

# ==============================================================================================================


# =================================================================================================================
#                                                   Filtering  
# =================================================================================================================

# 1. SETUP: Create a sample array of data (numbers 10 through 100, step 10)
data = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
print('=' * 100)
print(f"Original Array: {data}")
print("-" * 30)

# --- METHOD 1: Boolean Indexing (The most common way) ---

# Step A: Create a boolean mask
# We want to find numbers greater than 50.
# This creates a new array of True/False values.
mask = data > 50

print(f"Boolean Mask (data > 50): \n{mask}")

# Step B: Apply the mask to the original array
# Python will only keep elements where the index in 'mask' is True.
filtered_data = data[mask]

print(f"Result (Filtered Data): {filtered_data}")
print("-" * 30)


# --- METHOD 2: Direct Filtering (Shorthand) ---

# You don't need to create a variable for the mask first.
# You can put the condition directly inside the brackets.
evens_only = data[data % 20 == 0] # Filter for numbers divisible by 20

print(f"Direct Filter (Divisible by 20): {evens_only}")
print("-" * 30)


# --- METHOD 3: Using np.where() ---

# np.where() is useful if you want the INDICES of the valid items,
# or if you want to replace values (If True do X, if False do Y).

# Example: Get the indices (positions) where data is less than 40
indices = np.where(data < 40)

print(f"Indices where data < 40: {indices[0]}")
print(f"Values at those indices: {data[indices]}")

# Example: Replace values based on a filter
# If data > 50, keep it. If not, replace it with 0.
replaced_data = np.where(data > 50, data, 0)

print(f"Replaced Data (Keep > 50, others become 0): {replaced_data}")






import numpy as np

# ======================================================================================================
#                                   NUMPY RANDOM MODULE EXPLAINED
# ======================================================================================================

print("\n" + "=" * 50)
print("NUMPY RANDOM NUMBER GENERATION")
print("=" * 50)

# Using default_rng() is the modern, recommended way to generate random numbers in NumPy.
# It creates a Generator instance, which is thread-safe and has better statistical properties
# than the legacy `np.random.seed()` method.
rng = np.random.default_rng()

fruits = np.array(["apple", "banana", "cherry", "date", "elderberry"])
print("=" * 40)
print("random choice from array ")
print("Original Array: ", fruits)
print("-" * 30)
print("Random choice: ", rng.choice(fruits))
print("-" * 30)
print("Random choices: ", rng.choice(fruits, size=3))
print("-" * 30)
print("Original Array: ", fruits)


print("=" * 40)
print("random float between 0 and 10")
print("-" * 30)
print (np.random.uniform(0, 10))
print("-" * 30)
print (np.random.uniform(0, 10, size=3))
print("-" * 30)
print (np.random.uniform(0, 10, size=(3, 3)))


print("=" * 40)
print("random int between 0 and 10 ")
print("-" * 30)
print (np.random.randint(0, 10))
print("-" * 30)
print (np.random.randint(0, 10, size=3))
print("-" * 30)
print (np.random.randint(0, 10, size=(3, 3)))
print("-" * 30)


# Explaining random.seed 
print("random.seed is for making the random numbers reproducible means same random numbers")
np.random.seed(0)
print(np.random.randint(0, 10, size=3))
np.random.seed(0)
print(np.random.randint(0, 10, size=3))


# Explaining random.default_rng.shuffle
# 1. Initialize the generator
rng = np.random.default_rng(seed=1) # Seed ensures reproducibility

# 2. Shuffling a simple list-like array
simple_arr = np.array([10, 20, 30, 40, 50])
rng.shuffle(simple_arr)
print(f"Shuffled 1D: {simple_arr}")

# 3. Shuffling a 2D array (Shuffles ROWS only)
matrix = np.array([[1, 1, 1], 
                   [2, 2, 2], 
                   [3, 3, 3]])

# NOTE: shuffle modifies the array IN-PLACE.
rng.shuffle(matrix)
print("\nShuffled Matrix (rows swapped, content stayed same):")
print(matrix) 



# =================================================================================================================
#                       🚀 IMPORTANT ARRAY CREATION FUNCTIONS (MISSING FROM CHEAT SHEET)
# =================================================================================================================

print("\n" + "=" * 60)
print("ARRAY CREATION FUNCTIONS")
print("=" * 60)

# ------------------------------------------------------------------------------
# np.arange([start,] stop[, step, dtype]) — Like Python's range(), but returns an ndarray.
# Creates evenly spaced values within a given interval.
# ------------------------------------------------------------------------------
print("\n--- np.arange() ---")
# np.arange(stop): 0 to stop-1
arr_arange = np.arange(5)
print(f"np.arange(5)              -> {arr_arange}")  # [0 1 2 3 4]

# np.arange(start, stop): start to stop-1
arr_arange2 = np.arange(2, 7)
print(f"np.arange(2, 7)           -> {arr_arange2}")  # [2 3 4 5 6]

# np.arange(start, stop, step): with custom step size
arr_arange3 = np.arange(0, 1, 0.2)
print(f"np.arange(0, 1, 0.2)      -> {arr_arange3}")  # [0.  0.2 0.4 0.6 0.8]

# np.arange with dtype
arr_arange4 = np.arange(5, dtype=float)
print(f"np.arange(5, dtype=float) -> {arr_arange4}")  # [0. 1. 2. 3. 4.]


# ------------------------------------------------------------------------------
# np.zeros(shape, dtype) — Create an array filled with 0s.
# ------------------------------------------------------------------------------
print("\n--- np.zeros() ---")
zeros_1d = np.zeros(4)
print(f"np.zeros(4)              -> {zeros_1d}")  # [0. 0. 0. 0.]

zeros_2d = np.zeros((2, 3))
print(f"np.zeros((2, 3))        ->\n{zeros_2d}")
# [[0. 0. 0.]
#  [0. 0. 0.]]

zeros_int = np.zeros(3, dtype=int)
print(f"np.zeros(3, dtype=int)  -> {zeros_int}")  # [0 0 0]


# ------------------------------------------------------------------------------
# np.ones(shape, dtype) — Create an array filled with 1s.
# ------------------------------------------------------------------------------
print("\n--- np.ones() ---")
ones_1d = np.ones(5)
print(f"np.ones(5)               -> {ones_1d}")  # [1. 1. 1. 1. 1.]

ones_2d = np.ones((3, 2))
print(f"np.ones((3, 2))         ->\n{ones_2d}")
# [[1. 1.]
#  [1. 1.]
#  [1. 1.]]


# ------------------------------------------------------------------------------
# np.full(shape, fill_value, dtype) — Create an array filled with a custom value.
# ------------------------------------------------------------------------------
print("\n--- np.full() ---")
full_arr = np.full(4, 7)
print(f"np.full(4, 7)            -> {full_arr}")  # [7 7 7 7]

full_2d = np.full((2, 3), 42)
print(f"np.full((2, 3), 42)     ->\n{full_2d}")
# [[42 42 42]
#  [42 42 42]]


# ------------------------------------------------------------------------------
# np.empty(shape) — Create an uninitialized array (contents are garbage/random).
# Faster than zeros/ones when you plan to overwrite every element.
# ------------------------------------------------------------------------------
print("\n--- np.empty() ---")
empty_arr = np.empty((2, 3))
print(f"np.empty((2, 3))        ->\n{empty_arr}")
# (contents are whatever was in memory — DO NOT assume zeros!)


# ------------------------------------------------------------------------------
# np.linspace(start, stop, num) — Create evenly spaced numbers over a specified interval.
# Unlike arange, you specify HOW MANY points, not the step size.
# The endpoint is INCLUDED by default (unlike arange).
# ------------------------------------------------------------------------------
print("\n--- np.linspace() ---")
lin_arr = np.linspace(0, 1, 5)
print(f"np.linspace(0, 1, 5)     -> {lin_arr}")  # [0.   0.25 0.5  0.75 1.  ]

lin_arr2 = np.linspace(0, 10, 4)
print(f"np.linspace(0, 10, 4)   -> {lin_arr2}")  # [ 0.          3.33333333  6.66666667 10.        ]

# Exclude endpoint with endpoint=False
lin_arr3 = np.linspace(0, 1, 4, endpoint=False)
print(f"np.linspace(0, 1, 4, endpoint=False) -> {lin_arr3}")  # [0.   0.25 0.5  0.75]


# ------------------------------------------------------------------------------
# np.eye(N, M, k, dtype) — Create a 2D identity matrix (ones on diagonal, zeros elsewhere).
# ------------------------------------------------------------------------------
print("\n--- np.eye() ---")
eye_3 = np.eye(3)
print(f"np.eye(3):\n{eye_3}")
# [[1. 0. 0.]
#  [0. 1. 0.]
#  [0. 0. 1.]]

eye_2x4 = np.eye(2, 4)
print(f"\nnp.eye(2, 4):\n{eye_2x4}")
# [[1. 0. 0. 0.]
#  [0. 1. 0. 0.]]

eye_offset = np.eye(4, k=1)  # offset diagonal by 1 (k=1 = above main diagonal)
print(f"\nnp.eye(4, k=1):\n{eye_offset}")
# [[0. 1. 0. 0.]
#  [0. 0. 1. 0.]
#  [0. 0. 0. 1.]
#  [0. 0. 0. 0.]]


# ------------------------------------------------------------------------------
# np.identity(n) — Identity matrix (square). Simpler but less flexible than np.eye.
# ------------------------------------------------------------------------------
print("\n--- np.identity() ---")
identity_4 = np.identity(4)
print(f"np.identity(4):\n{identity_4}")
# [[1. 0. 0. 0.]
#  [0. 1. 0. 0.]
#  [0. 0. 1. 0.]
#  [0. 0. 0. 1.]]


# ------------------------------------------------------------------------------
# np.zeros_like(), np.ones_like(), np.full_like() — Create arrays matching
# the shape & dtype of an existing array, filled with the given value.
# ------------------------------------------------------------------------------
print("\n--- *_like() functions ---")
template = np.array([[1, 2], [3, 4]])
print(f"Template array:\n{template}")

z_like = np.zeros_like(template)
print(f"\nnp.zeros_like(template):\n{z_like}")  # [[0 0] [0 0]]

o_like = np.ones_like(template)
print(f"\nnp.ones_like(template):\n{o_like}")  # [[1 1] [1 1]]

f_like = np.full_like(template, 99)
print(f"\nnp.full_like(template, 99):\n{f_like}")  # [[99 99] [99 99]]



# =================================================================================================================
#                       🚀 IMPORTANT ARRAY MANIPULATION (MISSING FROM CHEAT SHEET)
# =================================================================================================================

print("\n" + "=" * 60)
print("ARRAY MANIPULATION")
print("=" * 60)

# ------------------------------------------------------------------------------
# np.reshape(a, newshape) — Change the shape of an array without changing its data.
# Returns a VIEW when possible (memory is shared), not a copy.
# The new shape must be compatible with the original size.
# Use -1 for one dimension to let NumPy infer the size automatically.
# ------------------------------------------------------------------------------
print("\n--- np.reshape() ---")
arr_to_reshape = np.arange(12)
print(f"Original (1D):           {arr_to_reshape}")  # [ 0  1  2  3  4  5  6  7  8  9 10 11]

reshaped = np.reshape(arr_to_reshape, (3, 4))
print(f"Reshaped to (3, 4):\n{reshaped}")
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]]

# Using -1 (auto-infer): reshape to 4 columns, infer rows
auto_shape = np.reshape(arr_to_reshape, (-1, 4))
print(f"\nnp.reshape(arr, (-1, 4)):\n{auto_shape}")
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]]

# Can also use .reshape() method
reshaped2 = arr_to_reshape.reshape(2, 6)
print(f"\narr.reshape(2, 6):\n{reshaped2}")
# [[ 0  1  2  3  4  5]
#  [ 6  7  8  9 10 11]]


# ------------------------------------------------------------------------------
# .T / np.transpose() — Transpose an array (swap rows and columns).
# Returns a VIEW (no copy made).
# ------------------------------------------------------------------------------
print("\n--- .T / np.transpose() ---")
mat = np.array([[1, 2, 3], [4, 5, 6]])
print(f"Original (2, 3):\n{mat}")

print(f"\nTransposed via .T (3, 2):\n{mat.T}")
# [[1 4]
#  [2 5]
#  [3 6]]

print(f"\nTransposed via np.transpose():\n{np.transpose(mat)}")
# Same result


# ------------------------------------------------------------------------------
# np.sort(a, axis) — Sort array elements in ascending order.
# Returns a sorted COPY; original is unchanged.
# ------------------------------------------------------------------------------
print("\n--- np.sort() ---")
unsorted = np.array([3, 1, 4, 1, 5, 9, 2, 6])
print(f"Original unsorted:       {unsorted}")
sorted_arr = np.sort(unsorted)
print(f"np.sort(unsorted):       {sorted_arr}")  # [1 1 2 3 4 5 6 9]
print(f"Original unchanged:      {unsorted}")  # Original is safe

# Sorting 2D arrays: axis=0 sorts each column, axis=1 sorts each row
mat_sort = np.array([[3, 2, 1], [6, 5, 4]])
print(f"\n2D array:\n{mat_sort}")
print(f"\nSorted along axis=0 (sort each column):\n{np.sort(mat_sort, axis=0)}")
# [[3 2 1]
#  [6 5 4]]  (already sorted, each column is ascending)

print(f"\nSorted along axis=1 (sort each row):\n{np.sort(mat_sort, axis=1)}")
# [[1 2 3]
#  [4 5 6]]

# Sort in descending order: use [::-1] slicing on the result
desc_sorted = np.sort(unsorted)[::-1]
print(f"\nDescending sort:         {desc_sorted}")  # [9 6 5 4 3 2 1 1]


# ------------------------------------------------------------------------------
# np.ravel(a) — Flatten array to 1D. Returns a VIEW if possible (memory shared).
# np.flatten() — Same but ALWAYS returns a COPY (more predictable, uses more memory).
# ------------------------------------------------------------------------------
print("\n--- np.ravel() vs np.flatten() ---")
mat_flat = np.array([[1, 2, 3], [4, 5, 6]])
print(f"Original:\n{mat_flat}")

raveled = np.ravel(mat_flat)
print(f"np.ravel(mat) -> {raveled}")  # [1 2 3 4 5 6]

flattened = mat_flat.flatten()
print(f"mat.flatten() -> {flattened}")  # [1 2 3 4 5 6]

# KEY DIFFERENCE: ravel returns a VIEW (modifying it affects original!)
raveled[0] = 999
print(f"\nAfter modifying raveled[0] = 999:")
print(f"raveled:              {raveled}")
print(f"Original affected?:   \n{mat_flat}")  # YES! [[999   2   3] [  4   5   6]]

# flatten returns a COPY (modifying it does NOT affect original)
mat_flat2 = np.array([[1, 2], [3, 4]])
flat_copy = mat_flat2.flatten()
flat_copy[0] = 888
print(f"\nAfter modifying flat_copy[0] = 888:")
print(f"flat_copy:            {flat_copy}")
print(f"Original affected?:   \n{mat_flat2}")  # NO! [[1 2] [3 4]]


# ------------------------------------------------------------------------------
# np.concatenate((a1, a2, ...), axis) — Join a sequence of arrays along an existing axis.
# All arrays must have the same shape (except along the concatenation axis).
# ------------------------------------------------------------------------------
print("\n--- np.concatenate() ---")
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6]])

# Concatenate along axis=0 (add rows) — requires matching column count
cat_rows = np.concatenate((a, b), axis=0)
print(f"Concatenate along axis=0 (add rows):\n{cat_rows}")
# [[1 2]
#  [3 4]
#  [5 6]]

# Concatenate along axis=1 (add columns) — requires matching row count
# b needs to be transposed or same number of rows
c = np.array([[5], [6]])
cat_cols = np.concatenate((a, c), axis=1)
print(f"\nConcatenate along axis=1 (add columns):\n{cat_cols}")
# [[1 2 5]
#  [3 4 6]]


# ------------------------------------------------------------------------------
# np.vstack(tup) — Vertically stack arrays (row-wise). Same as concatenate along axis=0.
# More convenient: doesn't require matching dimensions — auto-converts 1D to 2D rows.
# ------------------------------------------------------------------------------
print("\n--- np.vstack() ---")
a_v = np.array([1, 2, 3])
b_v = np.array([4, 5, 6])
v_stacked = np.vstack((a_v, b_v))
print(f"np.vstack(([1,2,3], [4,5,6])):\n{v_stacked}")
# [[1 2 3]
#  [4 5 6]]


# ------------------------------------------------------------------------------
# np.hstack(tup) — Horizontally stack arrays (column-wise). Same as concatenate along axis=1.
# ------------------------------------------------------------------------------
print("\n--- np.hstack() ---")
a_h = np.array([1, 2, 3])
b_h = np.array([4, 5, 6])
h_stacked = np.hstack((a_h, b_h))
print(f"np.hstack(([1,2,3], [4,5,6])): {h_stacked}")  # [1 2 3 4 5 6]

# Can also combine 2D arrays
h_stacked_2d = np.hstack((a.reshape(2, -1), c))
print(f"\nnp.hstack on 2D arrays:\n{h_stacked_2d}")


# ------------------------------------------------------------------------------
# np.array_split(ary, indices_or_sections, axis) — Split array into multiple sub-arrays.
# np.split() — Same but requires equal division (raises error if not possible).
# ------------------------------------------------------------------------------
print("\n--- np.array_split() ---")
arr_split = np.arange(10)
print(f"Original: {arr_split}")

splits = np.array_split(arr_split, 3)
print(f"np.array_split(arr, 3):")
for i, s in enumerate(splits):
    print(f"  Part {i}: {s}")
# Part 0: [0 1 2 3]
# Part 1: [4 5 6]
# Part 2: [7 8 9]

# np.split requires equal division
try:
    np.split(arr_split, 3)
except ValueError as e:
    print(f"\nnp.split(arr, 3) raises: {e}")  # error because 10 isn't divisible by 3


# ------------------------------------------------------------------------------
# np.copy(a) / .copy() — Explicitly create a copy of an array.
# Essential when you need to avoid modifying the original.
# ------------------------------------------------------------------------------
print("\n--- np.copy() / .copy() ---")
original = np.array([1, 2, 3, 4])
copied = np.copy(original)
copied[0] = 99
print(f"Original:      {original}")  # [1 2 3 4]  — unchanged!
print(f"Modified copy: {copied}")    # [99 2 3 4]

# Same as .copy() method
copied2 = original.copy()



# =================================================================================================================
#                       🚀 ARRAY PROPERTIES & DTYPES (MISSING FROM CHEAT SHEET)
# =================================================================================================================

print("\n" + "=" * 60)
print("ARRAY PROPERTIES & DATA TYPES")
print("=" * 60)

arr_props = np.array([[1, 2, 3], [4, 5, 6]], dtype=np.int32)

print(f"Array:\n{arr_props}")
print(f"{"-" * 40}")

# dtype — The data type of the array elements
print(f".dtype       -> {arr_props.dtype}")       # int32

# shape — Tuple of array dimensions (rows, columns, ...)
print(f".shape       -> {arr_props.shape}")      # (2, 3)

# ndim — Number of dimensions (axes)
print(f".ndim        -> {arr_props.ndim}")       # 2

# size — Total number of elements
print(f".size        -> {arr_props.size}")       # 6

# itemsize — Size (in bytes) of each element
print(f".itemsize    -> {arr_props.itemsize} bytes")  # 4 (int32 = 4 bytes)

# nbytes — Total memory consumed by the array (size * itemsize)
print(f".nbytes      -> {arr_props.nbytes} bytes")    # 24

# .real / .imag — Real and imaginary parts (for complex arrays)
complex_arr = np.array([1+2j, 3+4j, 5+6j])
print(f"\nComplex array:           {complex_arr}")
print(f".real -> {complex_arr.real}")  # [1. 3. 5.]
print(f".imag -> {complex_arr.imag}")  # [2. 4. 6.]

# ------------------------------------------------------------------------------
# Common NumPy Data Types
# ------------------------------------------------------------------------------
print("\n--- Common NumPy Data Types ---")
print(f"np.int8    : 1-byte integer      (-128 to 127)")
print(f"np.int16   : 2-byte integer      (-32,768 to 32,767)")
print(f"np.int32   : 4-byte integer      (-2^31 to 2^31-1)")
print(f"np.int64   : 8-byte integer      (-2^63 to 2^63-1)")
print(f"np.uint8   : 1-byte unsigned     (0 to 255)")
print(f"np.float32 : 4-byte float        (~7 decimal digits)")
print(f"np.float64 : 8-byte float        (~15 decimal digits) — DEFAULT")
print(f"np.bool_   : Boolean (True/False)")
print(f"np.complex64  : 8-byte complex   (real+imag each 4 bytes)")
print(f"np.complex128 : 16-byte complex  (real+imag each 8 bytes) — DEFAULT")

# Changing dtype with astype()
float_arr = np.array([1.5, 2.7, 3.1])
int_arr = float_arr.astype(np.int32)
print(f"\nfloat_arr:           {float_arr}")
print(f"float_arr.astype(int32) -> {int_arr}")  # [1 2 3] — truncates decimals!



# =================================================================================================================
#                       🚀 ADDITIONAL UFUNCS & MATH (MISSING FROM CHEAT SHEET)
# =================================================================================================================

print("\n" + "=" * 60)
print("ADDITIONAL UFUNCS & MATH")
print("=" * 60)

arr_u = np.array([1, 2, 3, 4, 5])

# np.power(a, b) — Raise each element to a power (same as **)
print(f"np.power(arr, 2)     -> {np.power(arr_u, 2)}")  # [ 1  4  9 16 25]

# np.mod(a, b) — Element-wise remainder (same as %)
print(f"np.mod(arr, 3)       -> {np.mod(arr_u, 3)}")    # [1 2 0 1 2]

# np.remainder(a, b) — Same as np.mod
print(f"np.remainder(arr, 3) -> {np.remainder(arr_u, 3)}")  # [1 2 0 1 2]

# np.sign(a) — Sign of each element (-1, 0, 1)
sign_arr = np.array([-5, 0, 8, -3])
print(f"np.sign([-5, 0, 8, -3]) -> {np.sign(sign_arr)}")  # [-1  0  1 -1]

# np.clip(a, min, max) — Clip (limit) values to a range
clip_arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(f"np.clip(arr, 3, 7)   -> {np.clip(clip_arr, 3, 7)}")
# [3 3 3 4 5 6 7 7 7] — values below 3 become 3, above 7 become 7

# np.reciprocal(a) — Element-wise reciprocal (1/x)
recip_arr = np.array([1., 2., 4., 5.])
print(f"np.reciprocal([1.,2.,4.,5.]) -> {np.reciprocal(recip_arr)}")
# [1.   0.5  0.25 0.2 ]



# =================================================================================================================
#                       🚀 LINEAR ALGEBRA (MISSING FROM CHEAT SHEET)
# =================================================================================================================

print("\n" + "=" * 60)
print("LINEAR ALGEBRA (np.linalg)")
print("=" * 60)

# ------------------------------------------------------------------------------
# np.linalg.inv(a) — Matrix inverse.
# A @ A_inv ≈ Identity matrix.
# Only works for square, non-singular (determinant ≠ 0) matrices.
# ------------------------------------------------------------------------------
print("\n--- np.linalg.inv() ---")
A = np.array([[1, 2], [3, 4]])
print(f"Matrix A:\n{A}")

A_inv = np.linalg.inv(A)
print(f"\nInverse of A:\n{A_inv}")
# [[-2.   1. ]
#  [ 1.5 -0.5]]

# Verify: A @ A_inv ≈ I
identity_check = A @ A_inv
print(f"\nA @ A_inv (should be ≈ Identity):\n{identity_check}")
# [[1. 0.]
#  [0. 1.]]


# ------------------------------------------------------------------------------
# np.linalg.det(a) — Determinant of a square matrix.
# - If det = 0: matrix is singular (no inverse).
# - Useful for checking if a matrix is invertible.
# ------------------------------------------------------------------------------
print("\n--- np.linalg.det() ---")
print(f"det(A) = {np.linalg.det(A)}")  # -2.0000000000000004

B = np.array([[1, 2], [2, 4]])  # Singular matrix (rows are linearly dependent)
print(f"det(singular matrix B) = {np.linalg.det(B)}")  # 0.0


# ------------------------------------------------------------------------------
# np.linalg.eig(a) — Eigenvalues and eigenvectors.
# Returns (eigenvalues, eigenvectors).
# ------------------------------------------------------------------------------
print("\n--- np.linalg.eig() ---")
eig_vals, eig_vecs = np.linalg.eig(A)
print(f"Eigenvalues of A:       {eig_vals}")
print(f"Eigenvectors of A:\n{eig_vecs}")
# Each column of eig_vecs is an eigenvector corresponding to the eigenvalue at same index


# ------------------------------------------------------------------------------
# np.linalg.solve(A, b) — Solve linear system Ax = b.
# More efficient & numerically stable than computing inv(A) @ b.
# ------------------------------------------------------------------------------
print("\n--- np.linalg.solve() ---")
# Solve:
# 1x + 2y = 8
# 3x + 4y = 18
A_sys = np.array([[1, 2], [3, 4]])
b_sys = np.array([8, 18])

solution = np.linalg.solve(A_sys, b_sys)
print(f"Coefficient matrix A:\n{A_sys}")
print(f"Constants vector b:    {b_sys}")
print(f"Solution (x, y):       {solution}")  # [2. 3.]  → x=2, y=3

# Verify
print(f"Verification A @ x:    {A_sys @ solution}")  # [8. 18.] ✓


# ------------------------------------------------------------------------------
# np.linalg.norm(x, ord) — Matrix or vector norm.
# Default: Frobenius norm (for matrices) or L2 norm (for vectors).
# ------------------------------------------------------------------------------
print("\n--- np.linalg.norm() ---")
v = np.array([3, 4])
print(f"Vector [3, 4] L2 norm: {np.linalg.norm(v)}")  # 5.0 (√(3²+4²))

print(f"Vector [3, 4] L1 norm: {np.linalg.norm(v, ord=1)}")  # 7.0 (|3|+|4|)



# =================================================================================================================
#                       🚀 SAVE / LOAD ARRAYS (PERSISTENCE)
# =================================================================================================================

print("\n" + "=" * 60)
print("SAVING & LOADING ARRAYS")
print("=" * 60)

# ------------------------------------------------------------------------------
# np.save(file, arr) — Save a single array to a .npy file (binary, NumPy-specific format).
# np.load(file) — Load a .npy file back into an array.
# ------------------------------------------------------------------------------
print("\n--- np.save() / np.load() ---")
arr_save = np.array([10, 20, 30, 40, 50])
np.save('saved_array', arr_save)  # Creates 'saved_array.npy'
print(f"Saved array to 'saved_array.npy': {arr_save}")

# Load it back
loaded_arr = np.load('saved_array.npy')
print(f"Loaded array from 'saved_array.npy': {loaded_arr}")


# ------------------------------------------------------------------------------
# np.savetxt(file, arr) — Save array to a human-readable text file.
# np.loadtxt(file) — Load from text file.
# Good for portability (CSV format).
# ------------------------------------------------------------------------------
print("\n--- np.savetxt() / np.loadtxt() ---")
np.savetxt('saved_array.csv', arr_save, delimiter=',')
print(f"Saved to 'saved_array.csv': {arr_save}")

loaded_csv = np.loadtxt('saved_array.csv', delimiter=',')
print(f"Loaded from 'saved_array.csv': {loaded_csv}")



# =================================================================================================================
#                       🚀 SPECIAL VALUES & HANDLING
# =================================================================================================================

print("\n" + "=" * 60)
print("SPECIAL VALUES: NaN, Inf, isclose")
print("=" * 60)

# ------------------------------------------------------------------------------
# np.nan — IEEE 754 "Not a Number" (e.g., 0/0, sqrt(-1), missing data).
# np.inf — Infinity (e.g., 1/0).
# These propagate through calculations — any operation with NaN results in NaN.
# ------------------------------------------------------------------------------
print("\n--- np.nan & np.inf ---")
print(f"np.nan:                {np.nan}")       # nan
print(f"np.inf:                {np.inf}")       # inf
print(f"-np.inf:               {-np.inf}")      # -inf

# NaN poison: any operation with NaN → NaN
nan_arr = np.array([1, np.nan, 3, 4])
print(f"\nArray with NaN:        {nan_arr}")
print(f"nan_arr + 2:           {nan_arr + 2}")  # [3. nan 5. 6.]


# ------------------------------------------------------------------------------
# np.isnan(a) — Check element-wise for NaN.
# np.isfinite(a) — Check which elements are finite (not NaN, not Inf).
# np.isinf(a) — Check element-wise for Infinity.
# ------------------------------------------------------------------------------
print("\n--- np.isnan() / np.isfinite() / np.isinf() ---")
special_arr = np.array([1, np.nan, np.inf, 4, -np.inf])
print(f"Array:                 {special_arr}")
print(f"np.isnan(arr):         {np.isnan(special_arr)}")      # [False  True False False False]
print(f"np.isfinite(arr):      {np.isfinite(special_arr)}")   # [ True False False  True False]
print(f"np.isinf(arr):         {np.isinf(special_arr)}")      # [False False  True False  True]


# ------------------------------------------------------------------------------
# np.nan_to_num(a) — Replace NaN with 0, Inf with large finite numbers.
# np.nansum(), np.nanmean(), etc. — Aggregate functions that skip NaN values.
# ------------------------------------------------------------------------------
print("\n--- Handling NaN safely ---")
print(f"np.nan_to_num(arr):    {np.nan_to_num(special_arr)}")  # [1. 0. 1.79e+308 4. -1.79e+308]

print(f"\nnp.sum(arr):           {np.sum(nan_arr)}")           # nan (poisoned!)
print(f"np.nansum(arr):        {np.nansum(nan_arr)}")          # 8.0 (NaN skipped)
print(f"np.nanmean(arr):       {np.nanmean(nan_arr)}")         # 2.666...

# Other NaN-safe functions: np.nanmin(), np.nanmax(), np.nanstd(), np.nanvar()



# =================================================================================================================
#                       BONUS: ADVANCED INDEXING TIPS
# =================================================================================================================

print("\n" + "=" * 60)
print("ADVANCED INDEXING")
print("=" * 60)

# ------------------------------------------------------------------------------
# Fancy Indexing — Index with an array of integers to select rows/elements.
# Unlike slicing, fancy indexing ALWAYS returns a COPY, not a view.
# ------------------------------------------------------------------------------
print("\n--- Fancy Indexing ---")
fancy_arr = np.arange(10, 20)
print(f"Array: {fancy_arr}")

indices = np.array([0, 2, 5, 8])
print(f"Selected indices {indices}: {fancy_arr[indices]}")  # [10 12 15 18]

# 2D fancy indexing
mat_fancy = np.arange(1, 13).reshape(3, 4)
print(f"\n2D Array:\n{mat_fancy}")

# Select specific rows
row_indices = np.array([0, 2])
print(f"\nRows {row_indices}:\n{mat_fancy[row_indices]}")
# [[ 1  2  3  4]
#  [ 9 10 11 12]]


# ------------------------------------------------------------------------------
# np.argmax(a) / np.argmin(a) — Return the INDEX of the maximum/minimum value.
# ------------------------------------------------------------------------------
print("\n--- np.argmax() / np.argmin() ---")
test_arr = np.array([3, 1, 4, 1, 5, 9, 2, 6])
print(f"Array: {test_arr}")
print(f"Index of max:  {np.argmax(test_arr)}")  # 5 (value 9)
print(f"Index of min:  {np.argmin(test_arr)}")  # 1 (value 1)

# With axis on 2D
arg_2d = np.array([[3, 2, 5], [1, 7, 4]])
print(f"\n2D Array:\n{arg_2d}")
print(f"np.argmax(axis=0): {np.argmax(arg_2d, axis=0)}")  # [0 1 0] — max per column
print(f"np.argmax(axis=1): {np.argmax(arg_2d, axis=1)}")  # [2 1] — max per row



print("\n" + "=" * 60)
print("🎉 THAT'S ALL FOR NOW — HAPPY NUMPY CODING! 🎉")
print("=" * 60)
