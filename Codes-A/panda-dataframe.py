import pandas as pd

# Create a simple DataFrame:

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

#load data into a DataFrame object:
df = pd.DataFrame(data)
# print(df) 

# refer to the row index:
# print(df.loc[0])

# # Return row 0 and 1:
# print(df.loc[[0, 1]])

# Add a list of names to give each row a named-index:
data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

df = pd.DataFrame(data, index = ["day1", "day2", "day3"])
# print("Named Index:", df) 

#refer to the named index:
print("Refer named index:", df.loc["day2"])

