import pandas as pd  # Import the pandas library and alias it as 'pd' for standard usage
print(pd.__version__)


#=======================================================================================

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


#=======================================================================================
print ("\n" * 2)
print ("=" * 70)
print ("=" * 70)
print ("=" * 70)
print ("\n" * 2)


#=======================================================================================

# DataFrame is pandas two dimensional array think of it like multiple columns in spread sheet or exacl table in database 
import numpy as np # Imported only to create "Not a Number" (missing) values for the example

def DataFrames():
    print("=== STEP 1: CREATION & BASICS (Review) ===")
    data = {
        "Name": ["John", "Anna", "Peter", "Linda"],
        "Age": [28, 22, 34, 42],
        "City": ["New York", "Paris", "London", "Berlin"]
    }
    
    # Create the DataFrame
    df = pd.DataFrame(data, index=["a", "b", "c", "d"])
    
    # Add a column
    df["Country"] = ["USA", "France", "UK", "Germany"]
    
    # Add a row using concat
    new_row = pd.DataFrame([{"Name": "Ahmed", "Age": 28, "City": "Dubai", "Country": "UAE"}], index=['e'])
    df = pd.concat([df, new_row])
    
    print(df)
    print("\n" + "="*50 + "\n")


    print("=== STEP 2: INSPECTING DATA (Mandatory) ===")
    # Before processing, you must 'look' at your data without printing the whole thing.
    
    print("--- 1. Head (First 3 rows) ---")
    print(df.head(3)) # Useful if your table has 1 million rows
    
    print("\n--- 2. Info (Data Types & Non-Nulls) ---")
    # This is CRITICAL. It tells you if 'Age' is actually a number or stored as text (object).
    print(df.info()) 
    
    print("\n--- 3. Describe (Statistics) ---")
    # Gives you the mean, max, min, and standard deviation of numerical columns instantly.
    print(df.describe()) 
    print("\n" + "="*50 + "\n")


    print("=== STEP 3: DIRTY DATA & CLEANING (Mandatory) ===")
    # Let's purposefully break the data to show how to fix it.
    # We add a row with missing values (np.nan) and a duplicate row.
    dirty_row = pd.DataFrame([
        {"Name": "John", "Age": np.nan, "City": None, "Country": "USA"}, # Missing Age/City
        {"Name": "John", "Age": 28, "City": "New York", "Country": "USA"} # Duplicate of row 'a'
    ], index=['f', 'g'])
    
    df_dirty = pd.concat([df, dirty_row])
    print("--- The Dirty Table (Note the NaN and Duplicates) ---")
    print(df_dirty)
    print("\n")

    # 1. Dropping Duplicates
    df_clean = df_dirty.drop_duplicates(subset=["Name", "Country"]) 
    print("--- After drop_duplicates() ---")
    print(df_clean)
    print("\n")

    # 2. Handling Missing Values (NaN)
    # Option A: Drop rows with missing data
    # df_clean = df_clean.dropna() 
    
    # Option B: Fill missing data (Better for keeping data)
    # We fill missing numeric Age with the mean (average), and missing text with "Unknown"
    values_to_fill = {"Age": df["Age"].mean(), "City": "Unknown"}
    df_clean = df_clean.fillna(value=values_to_fill)
    
    print("--- After fillna() (Cleaning complete) ---")
    print(df_clean)
    print("\n" + "="*50 + "\n")


    print("=== STEP 4: FILTERING & QUERYING (Mandatory) ===")
    # This is like the SQL 'WHERE' clause.
    
    # Condition 1: People older than 30
    print("--- Filter: Age > 30 ---")
    print(df_clean[ df_clean["Age"] > 30 ])
    print("\n")
    
    # Condition 2: Multiple conditions (AND requires '&', OR requires '|')
    # Parentheses () are mandatory around each condition!
    print("--- Filter: Age > 25 AND Country is USA ---")
    condition = (df_clean["Age"] > 25) & (df_clean["Country"] == "USA")
    print(df_clean[condition])
    print("\n" + "="*50 + "\n")


    print("=== STEP 5: SORTING & DROPPING (Mandatory) ===")
    
    # Sorting by values
    # ascending=False means High to Low
    print("--- Sorted by Age (Oldest to Youngest) ---")
    print(df_clean.sort_values(by="Age", ascending=False))
    print("\n")

    # Dropping a Column we don't need
    # axis=1 refers to Columns (vertical). axis=0 refers to Rows (horizontal).
    print("--- Dropping the 'City' Column ---")
    df_dropped = df_clean.drop("City", axis=1)
    print(df_dropped)
    print("\n" + "="*50 + "\n")


    print("=== STEP 6: GROUPING & AGGREGATION (The most powerful feature) ===")
    # This allows you to group data by a category and get stats (like a Pivot Table).
    
    # Let's add more data to make grouping meaningful
    more_data = pd.DataFrame([
        {"Name": "Sara", "Age": 25, "Country": "USA"},
        {"Name": "Tom", "Age": 35, "Country": "UK"}
    ])
    df_group = pd.concat([df_dropped, more_data], ignore_index=True)

    print("--- Data for Grouping ---")
    print(df_group)
    print("\n")

    # Question: What is the average Age per Country?
    # 1. Group by Country
    # 2. Select the 'Age' column
    # 3. Calculate the mean()
    print("--- Average Age per Country ---")
    print(df_group.groupby("Country")["Age"].mean())
    print("\n")

    # Count how many people are in each country
    print("--- Count of people per Country ---")
    print(df_group["Country"].value_counts())
    print("\n" + "="*50 + "\n")
    
    print("Code finished successfully. (File save commented out to prevent error)")
    print("\n" + "="*70 + "\n")

# Run the DataFrames Guide
DataFrames()
#=======================================================================================


def LearnFilesReading ():
    # CSV FILES
    print("CSV FILES")
    df = pd.read_csv("/home/mohammed_bahr/Projects/DataBase/Pandas/people.csv")
    print(df)
    print("\n" + "-"*30 + "\n")
    print("if You Want to print all data use df.to_string()")
    print(df.to_string())
    print("\n" + "-"*30 + "\n")
    print("if You Want to print first 5 rows use df.head(5)")
    print(df.head(5))
    print("\n" + "-"*30 + "\n")
    print("if You Want to print last 5 rows use df.tail(5)")
    print(df.tail(5))
    print("\n" + "-"*30 + "\n")

    print("\n" + "="*70 + "\n")
    # JSON FILES
    print ("JSON FILES")
    df_json = pd.read_json("/home/mohammed_bahr/Projects/DataBase/Pandas/titanic.json")
    print(df_json)
    print("\n" + "-"*30 + "\n")
    print("if You Want to print all data use df.to_string()")
    print(df_json.to_string())
    print("\n" + "-"*30 + "\n")
    print("if You Want to print first 5 rows use df.head(5)")
    print(df_json.head(5))
    print("\n" + "-"*30 + "\n")
    print("if You Want to print last 5 rows use df.tail(5)")
    print(df_json.tail(5))
    print("\n" + "-"*30 + "\n")


    print("\n" + "="*70 + "\n")
    # ============================================================================================================
    #                                             Selection by Column
    # ============================================================================================================
    print("we will just working with csv but it's same process for all files")
    print("\n" + "="*70 + "\n")
    
    print("First Name column from csv file")
    print(df["First Name"])
    print("\n" + "-"*30 + "\n")


    print("First Name and Phone and Gender -> ")
    print(df[["First Name", "Phone", "Gender"]])
    print("\n" + "-"*30 + "\n")


    # ============================================================================================================
    #                                             Selection by Rows
    # ============================================================================================================

    # loc[] -> Selection by Label
    print("Selection by Label") # since we didn't assign andy indexing its counts from 0 to n by deafult 
    print(df.loc[4])
    print("\n" + "-"*30 + "\n")

    # iloc[] -> Selection by Index
    print("Selection by Index")
    print(df.iloc[4])
    print("\n" + "-"*30 + "\n")

    # we can change its labol to be any column we want using index_col i
    df_new = pd.read_csv("/home/mohammed_bahr/Projects/DataBase/Pandas/people.csv", index_col="First Name") # it will make the First Name column as index
    print(df_new)
    print("\n" + "-"*30 + "\n")
    print(df_new.loc["Lindsey"])
    print("\n" + "-"*30 + "\n")
    print(df_new.iloc[4])
    print("\n" + "-"*30 + "\n")

    print("you can also select specific columns for one index row using loc or iloc")
    print(df_new.loc["Lindsey", ["Gender","Phone",]])
    print("\n" + "-"*30 + "\n")
    print(df_new.iloc[4, [1, 2]])
    print("\n" + "-"*30 + "\n")

    print("you can also select specific number of rows and columns")
    print(df.loc[0:9]) # remember that the last number is exclusive then it will return from 0 to 9 rows 
    print("\n" + "-"*30 + "\n")
    # iloc[start:end:step] -> step is the number of rows to skip
    print(df_new.iloc[0:10:2]) # remember that the last number is exclusive then it will return from 0 to 10 rows 
    print("\n" + "-"*30 + "\n")

    # ============================================================================================================
    #                                            Filtering -> Selection by Condition
    # ============================================================================================================
    print("Selection by Condition")
    Engineers = df[df["Gender"]== "Female"]
    target = df[df["Index"] > 500]
    print(Engineers)
    print(target)
    print("\n" + "-"*30 + "\n")

    print("you can also use multiple conditions like to be female and job title contains engineer")
    # Select females whose job title contains the word "engineer"
    female_engineers = df[
        (df["Gender"] == "Female") & 
        (df["Job Title"].str.strip().str.lower().str.contains("engineer"))
    ]
    print(female_engineers)
    print("\n" + "-"*30 + "\n")
  

LearnFilesReading()
