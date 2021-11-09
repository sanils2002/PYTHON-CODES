import pandas as pd

df = pd.read_csv('D:\IIIT Nagpur\IT Workshop1\pandas\StudentsPerformance1.csv')
# Removing row containing missing value

#new_df = df.dropna()
#print(new_df.to_string())

# to change the original DataFrame
#df.dropna(inplace = True)
#print(df.to_string())

# The fillna() method allows us to replace empty cells with a value
#df = pd.read_csv('D:\IIIT Nagpur\IT Workshop1\pandas\StudentsPerformance4.csv')
#df.fillna(130, inplace = True)
#print(df.to_string())

# Filling a specific value in a specific column
df = pd.read_csv('D:\IIIT Nagpur\IT Workshop1\pandas\StudentsPerformance4.csv')
#df["math score"].fillna(130, inplace = True)
#print(df.to_string())

# Filling the value of mean 
x = df["reading score"].mean()             # Mean = the average value
df["reading score"].fillna(x, inplace = True)
print(df.to_string())

# # Filling the value of median 
#x = df["writing score"].median()           #  Median = the value in the middle, after you have sorted all values ascending.
# df["writing score"].fillna(x, inplace = True)
# print(df.to_string())


#x = df["writing score"].mode()[0]      #  the value that appears most frequently ([0] because it returns series having only one value)
# # print(x)           
# df["writing score"].fillna(x, inplace = True)
# print(df.to_string())

# df.loc[6, 'math score'] = 88
# print(df.to_string())

for x in df.index:
   if df.loc[x, "math score"] > 100:
     df.loc[x, "math score"] = 100

# print(df.to_string())

# for x in df.index:
#   if df.loc[x, "math score"] > 100:
#     df.drop(x, inplace = True)      # Remove the row

# print(df.to_string())
# print(df.duplicated())   #  Returns True for every row that is a duplicate, othwerwise False

#df.drop_duplicates(inplace = True)  # Drop Duplicates

#print(df.corr())   # The corr() method calculates the relationship between each column in your data set.