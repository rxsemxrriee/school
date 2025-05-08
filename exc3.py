import numpy as np

row = int(input("Enter the row count of the array: "))
column = int(input("Enter the column count of the array: "))
afloat = float(input("Enter a float: "))

def user_array(row,column,afloat):
    arr = np.full((row,column),afloat)
    return arr

print(user_array(row,column,afloat))