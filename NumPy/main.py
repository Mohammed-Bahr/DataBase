import numpy as np

# print the numpy version
print("Numpy version: ", np.__version__)

#                                         create a numpy array 
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
