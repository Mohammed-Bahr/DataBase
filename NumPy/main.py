import numpy as np

# print the numpy version
print("Numpy version: ", np.__version__)

#                                         create a numpy array 
#                                      Scalar Arithmetic Operations
arr = np.array([1, 2, 3, 4, 5])
print("Numpy array: ", arr)
 # multiply the array by 2
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
#                                          Array Manipulation
#--------------------------------------------------------------------------------------------------

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
#/ !=  Not equal to

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

# then axis is the one who decide whether to work on rows (axis = 1) or columns (axis = 0)

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




