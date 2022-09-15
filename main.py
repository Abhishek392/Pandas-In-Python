import pandas as pd
import numpy as np

# # Series: A Pandas Series is like a column in a table. It is a one-dimensional array holding data of any type.
# # syntax: pd.Series(linear data structure or key/value object)
# arr = np.array([2, 9, 8, 3])
# ser = pd.Series(arr)
# print(ser)
# # If nothing else is specified, the values are labeled with their index number. First value has index 0,second value has
# # index 1 etc.
# print("Value at label 0 is: ", ser[0])  # series[l] will return the value at label = l
# ser = pd.Series(arr, index=["x", "y", "z", "t"])  # With the index argument, you can name your own labels.
# print(ser)
# # key/value object like dictionary
# dict = {"Name":"Abhishek", "SAP":500096952, "Roll_No":"R2142211227"}
# ser = pd.Series(dict) # the keys of dictionary becomes the label
# print(ser)



# # Dataframe: A Pandas DataFrame is a 2 dimensional data structure, like a 2 dimensional array, or a table with rows and
# # columns.
# data = {
#   "calories": [420, 380, 390],
#   "duration": [50, 40, 45]
# }
# dataframe = pd.DataFrame(data)
# print(dataframe)
# # Locate Row: Pandas use the loc attribute to return one or more specified row(s)
# print(dataframe.loc[0]) # it will print the row with index 0.
# print(dataframe.loc[[0, 1]]) # it will print the row with index 0 and 1
# # Named Index
# dataframe = pd.DataFrame(data, index = ["day1", "day2", "day3"])
# print(dataframe)
# # dataframe to csv file
# dataframe.to_csv("plan.csv") # create the plan.csv with indexes in the working directory.
# dataframe.to_csv("plan_without_index.csv", index=False) # create the file without indexes in the working directory
# # head and tail
# print(dataframe.head(1)) # show first row only
# print(dataframe.tail(1)) # show last row only



# # Read csv file
# dataframe = pd.read_csv("iris.csv")
# print(dataframe)
# # Use to_string() to print the entire DataFrame.
# print(dataframe.to_string())
# # Transpose of dataframe
# print(dataframe.T)
# # Change the value: dataframe[column_label][row_label] = changed value
# dataframe["SepalLengthCm"][0] = 5
# print(dataframe)



# # Analyzing Data
# # head and tail: The head() method returns the headers and a specified number of rows, starting from the top. if the
# # number of rows is not specified, the head() method will return the top 5 rows.
# dataframe = pd.read_csv("iris.csv")
# print(dataframe.head(1)) # show first row only
# print(dataframe.tail(1)) # show last row only
# # info: The DataFrames object has a method called info(), that gives you more information about the data set.
# print(dataframe.info()) # The info() method also tells us how many non-Null values there are present in each column, and
# # in our data set it seems like all the values are non-null.



# # Data Cleaning: Data cleaning means fixing bad data in your data set. Bad data could be empty cell, data in wrong
# # format, wrong data, duplicates.
# df = pd.read_csv("dataset.csv") # The data set contains some empty cells ("Date" in row 22, and "Calories" in row 18
# # and 28).The data set contains wrong format ("Date" in row 26).The data set contains wrong data ("Duration" in row 7).
# # The data set contains duplicates (row 11 and 12).

# # Empty cells: Empty cells can potentially give you a wrong result when you analyze data.
# # Remove rows: One way to deal with empty cells is to remove rows that contain empty cells.
# df = pd.read_csv("dataset.csv")
# new_df = df.dropna() # By default dropna will create the new dataframe and not change the original dataframe.
# df.dropna(inplace=True) # if you want to change the original dataframe, use inplace=True argument.
# print(new_df)
# # Replace Empty Values: Another way of dealing with empty cells is to insert a new value instead.
# df1 = pd.read_csv("dataset.csv")
# df1.fillna(130, inplace=True)
# print(df1)
# df2 = pd.read_csv("dataset.csv")
# df2["Calories"].fillna(130, inplace=True) # Replace Only For Specified Columns
# print(df2)

# # Wrong Format: Cells with data of wrong format can make it difficult, or even impossible, to analyze data.To fix it,
# # you have two options: remove the rows, or convert all cells in the columns into the same format.
# # Remove Rows
# df = pd.read_csv("dataset.csv")
# df.dropna(subset = ['Calories'], inplace = True)
# print(df.to_string())

# # Wrong Data: "Wrong data" does not have to be "empty cells" or "wrong format", it can just be wrong, like if someone
# # registered "199" instead of "1.99".
# # Replacing Value
# df = pd.read_csv('dataset.csv')
# for x in df.index:
#   if df.loc[x, "Duration"] > 120:
#     df.loc[x, "Duration"] = 120
# print(df.to_string())
# # Removing Rows
# df1 = pd.read_csv("dataset.csv")
# for x in df.index:
#   if df1.loc[x, "Duration"] > 120:
#     df1.drop(x, inplace = True)
# print(df1.to_string())

# # Duplicates:
# # Discovering Duplicates
# df = pd.read_csv('dataset.csv')
# print(df.duplicated()) # Returns True for every row that is a duplicate, othwerwise False.
# # Removing Duplicates
# df.drop_duplicates(inplace = True)
# print(df.to_string())



# Imporatant
df = pd.DataFrame(np.random.rand(334, 5), index = np.arange(334))

# # sort index
# df.sort_index(axis = 0, ascending = False) # axis = 0 is row
# print(df)

# # copy of csv file
# df0 = df # here df0 points to df. So, when we change df0 then that changes reflect in df also.
# df1 = df.copy() # Here df doesn't change on changing df1

# # loc function
# df.loc[0, 0] = 3 # loc[rows, columns] = changed value, this is the best method to change the value.
# print(df)
# print(df.loc[[0, 1], [2, 3]])
# print(df.loc[[0, 1], :]) # : means all column
# print(df.loc[(df[0]<0.3) & df[3]>0.1])

# drop function
# df = df.drop(0, axis=1) # this will drop 0th column
# print(df)







































