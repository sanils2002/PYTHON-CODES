import pandas as pd

# printing the first 10 rows of the DataFrame

df = pd.read_csv('D:\\IIITN\\PhD\\Reinforcement_Learning_implementation\\Input_data_v2.csv')
print("Printing 10 lines")
print(df.head(10))

#############################

# Print the first 5 rows of the DataFrame

df = pd.read_csv('D:\\IIITN\\PhD\\Reinforcement_Learning_implementation\\Input_data_v2.csv')
# print("Printing 5 lines")
# print(df.head())

# Print the last 5 rows of the DataFrame
# print("Printing last 5 lines")
# print(df.tail()) 

# # Print information about the data
print("dataframe info")
print(df.info())