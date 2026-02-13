import pandas as pd 

print(pd.__version__)

import pandas as pd  # Import the pandas library and alias it as 'pd' for standard usage

def Series():
    """
    Function to demonstrate various Pandas Series creation and manipulation techniques.
    """
    
    # --- 1. Creating a Series from a List with Mixed Data Types ---
    # A standard Python list containing integers, floats, strings, and booleans.
    data = [100, 200.7, 300, "Hello", True] 

    # Convert the list into a Pandas Series.
    # Note: Pandas creates an 'object' dtype Series because the data is mixed.
    # 'Series' is capitalized because it is a Class Constructor (blueprint for creating objects).
    series = pd.Series(data) 
    print("--- Mixed Type Series ---")
    print(series)

    print("\n" * 2) # Print 2 new lines for spacing

    # --- 2. Creating a Series with a Custom Index ---
    # A standard list of homogenous (same type) integers.
    data2 = [100, 200, 300, 400, 500] 

    # Create a Series and explicitly define the index labels ('a' through 'e').
    # CRITICAL: The number of items in 'index' must match the number of items in 'data'.
    # If len(data) != len(index), Python will raise a ValueError.
    series2 = pd.Series(data2, index=["a", "b", "c", "d", "e"]) 
    print("--- Custom Indexed Series ---")
    print(series2)

    print('-' * 30) # Print a separator line

    # --- 3. Accessing Series Attributes ---
    # .index returns the index labels (RangeIndex or explicitly defined labels).
    print(f"Index: {series2.index}")
    # .values returns the underlying data as a numpy array.
    print(f"Values: {series2.values}")

    # --- 4. Selection: .loc vs .iloc ---
    # .loc[] looks up data by LABEL (Name). Here it looks for the row labeled "a".
    print(f"Value at label 'a': {series2.loc['a']}") 
    
    # .iloc[] looks up data by INTEGER POSITION (Index). 
    # 0 is the first item, 1 is the second, etc.
    print(f"Value at position 0: {series2.iloc[0]}") 

    print('-' * 30)

    # --- 5. Modifying Data ---
    # Updating the value associated with label "a" to 1000.
    series2.loc["a"] = 1000
    print(f"New value at 'a': {series2.loc['a']}")

    # Updating the value at the second position (index 1) to 2000.
    series2.iloc[1] = 2000
    print(f"New value at index 1: {series2.iloc[1]}")

    
    # --- 6. Boolean Indexing (Filtering) ---
    # Creating a large dataset of numbers 1-20.
    data3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

    # Creating a Series with a matching number of index labels (a-t).
    series3 = pd.Series(data3, index=[
        "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", 
        "k", "l", "m", "n", "o", "p", "q", "r", "s", "t"
    ])
    
    print("\n" * 2)
    print("-" * 70)
    
    # This is called "Boolean Masking" or "Filtering".
    # Logic:
    # 1. 'series3 > 10' creates a temporary Series of True/False values.
    # 2. 'series3[...]' only keeps the rows where the value was True.
    print("--- Values greater than 10 ---")
    print(series3[series3 > 10])


    print('=' * 70)

    # --- 7. Creating a Series from a Dictionary ---
    # Python dictionary with Key-Value pairs.
    calories = {"apple": 100, "banana": 200, "orange": 300, "grape": 400, "mango": 500}

    # When converting a Dict to a Series:
    # Keys become the Index.
    # Values become the Data.
    series4 = pd.Series(calories)
    print("--- Dictionary converted to Series ---")
    print(series4)

    print("\n")
    print("-" * 40)
    
    # Filtering the dictionary-based series for values > 200.
    print(series4[series4 > 200])

    # Retrieving a specific value using its label (Key).
    result = series4.loc["orange"]
    print("print orange value -> " + str(result))

# Call the function to run the code
Series()



print ("\n" * 2)
print ("=" * 70)
print ("=" * 70)
print ("=" * 70)
print ("\n" * 2)



# DataFrame is pandas two dimensional array think of it like multiple columns in spread sheet or exacl table in database 
def Data_Frame ():
    data = {
        "Name": ["John", "Anna", "Peter", "Linda"],
        "Age": [28, 22, 34, 42],
        "City": ["New York", "Paris", "London", "Berlin"]
    }

    df = pd.DataFrame(data) # DataFrame is case sensitive because it is a constructor  not function 
    print(df)
    print ("\n")
    print('-' * 30)
    print ("\n")
    data = {
        "Name": ["John", "Anna", "Peter", "Linda"],
        "Age": [28, 22, 34, 42],
        "City": ["New York", "Paris", "London", "Berlin"]
    }

    df = pd.DataFrame(data , index=["a" , "b" , "c" , "d"] ) # DataFrame is case sensitive because it is a constructor  not function 
    print(df)
    print ("\n")
    print('-' * 30)
    print ("\n")

    print (df.loc["c"]) # loc = location by labol this returns the value of the element at the given index  
    print ("\n")
    print ("-" * 30)
    print ("\n")
    print (df.iloc[2]) # iloc = location by index this returns the value of the element at the given index  
    print ("\n")
    print ("-" * 30)
    print ("\n")

    # adding a new column 
    df["Country"] = ["USA", "France", "UK", "Germany"]
    print(df)
    print ("\n")
    print ("-" * 30)
    print ("\n")

    # adding a new row 
    new_row = {"Name": "John", "Age": 28, "City": "New York", "Country": "USA"}
    df = pd.concat([df, pd.DataFrame([new_row])]) 
    print(df)
    print ("\n")
    print ("-" * 30)
    print ("\n")
    
    



Data_Frame()