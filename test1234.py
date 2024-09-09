import numpy as np
import pandas as pd

# Creating an array
# array_2d = np.array([[1, 2, 3], [4, 5, 6]])
# rownames = ['a', 'b']
# colnames = ['one', 'two', 'three']
# dataframe = pd.DataFrame(array_2d, index=rownames, columns=colnames)
# print(dataframe)
# print("Original array: \n", array_2d)

# # Series in pandas
# pandasSeries = pd.Series([1, 2, 3, 4, 5], index = ['a', 'b', 'c', 'd', 'e'])
# print(pandasSeries)
# print(pandasSeries['a'])
# print(pandasSeries + 2, pandasSeries.mean, pandasSeries.sum, pandasSeries.multiply)

# # Dataframes in pandas
# pandasDF = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
# print(pandasDF)
# print(pandasDF['A'])
# print(pandasDF.loc[0])

# Load data from a CSV file into a DataFrame
# df = pd.read_csv('mycsvfile.csv', usecols=[''])

# # Display the first 5 rows of the DataFrame
# print(df.head())

# Statistical Summary
# from pandas import read_csv
# url = 'https://goo.gl/bDdBiA'
# names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
# data = read_csv(url, names=names)
# description = data.describe()
# print(description)

# import csv

# Open the CSV file
# with open('mycsvfile.csv', mode='r') as file:
#     # Create a CSV reader object
#     csv_reader = csv.reader(file)
#     data = list(csv_reader)

#     # Loop through each row in the CSV
#     for row in csv_reader:
#         print(row)
    
# # Access the entire CSV as a list of lists
# print(data)

#Load the CSV file using numpy
data = np.loadtxt('mycsvfile.csv', delimiter=',', dtype=str, encoding='utf-8')

# Print the loaded data
print(data)
