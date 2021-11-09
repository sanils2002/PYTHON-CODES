import pandas as pd

# printing the first 10 rows of the DataFrame

df = pd.read_csv('D:\IIIT Nagpur\IT Workshop1\pandas\data.csv')
print(df.head(10))

#############################

# Print the first 5 rows of the DataFrame

df = pd.read_csv('D:\IIIT Nagpur\IT Workshop1\pandas\data.csv')
print(df.head())

# Print the last 5 rows of the DataFrame
print(df.tail()) 

# Print information about the data
print("Data frame info:")
print(df.info())