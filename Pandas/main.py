import pandas as pd 

print(pd.__version__)

# Series is pandas one dimensional array think of it like single column in spread sheet  
def Series ():
    data = [100 , 200.7 ,300 , "Hello" , True] # pandas array can hold multiple data types 

    series = pd.Series(data) # Series is case sensitive because it is a constructor  not function 
    print(series)

    print("\n" * 2)

    data2= [100 , 200 ,300 , 400 , 500] # pandas array can hold multiple data types 

    series2 = pd.Series(data2 , index=["a" , "b" , "c" , "d" , "e" ]) 
    # if data2 size is smaller or greater than index size it will give error 
    print(series2 )


    print ('-' * 30)

    print (series2.index)
    print (series2.values)

    print (series2.loc["a"]) # loc = location by labol this returns the value of the element at the given index  
    print(series2.iloc[0]) # iloc = location by index this returns the value of the element at the given index  

    print ('-' * 30)

    series2.loc["a"] = 1000
    print(series2.loc["a"])

    series2.iloc[1] = 2000
    print(series2.iloc[1])

    

    data3 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

    series3 = pd.Series(data3 , index=["a" , "b" , "c" , "d" , "e" , "f" , "g" , "h" , "i" , "j" , "k" , "l" , "m" , "n" , "o" , "p" , "q" , "r" , "s" , "t" ])
    print(series3)
    print("\n" * 2)
    print("-" * 70)
    print(series3[series3 > 10])


    print('=' * 70)


    calories = {"apple": 100 , "banana": 200 , "orange": 300 , "grape": 400 , "mango": 500}

    series4 = pd.Series(calories)
    print(series4)

    print("\n")
    print("-" * 40)
    print(series4[series4 > 200])

    result = series4.loc["orange"]
    print("print orange value -> " + str(result))




Data_Frame()


# DataFrame is pandas two dimensional array think of it like multiple columns in spread sheet or exacl table in database 
def Data_Frame ():
 