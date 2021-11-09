import pandas as pd

# a = [1, 7, 2]

# myvar = pd.Series(a)
# print("Series:",myvar)
# print("First value of sries:",myvar[0])

##########################################

# create user defines labels for series indices
# a = [1, 7, 2]

# myvar = pd.Series(a, index = ["x", "y", "z"])
# print("Series:",myvar)
# print("Value at index y:", myvar["y"])

# ##########################################

# Series from a dictionary

# calories = {"day1": 420, "day2": 380, "day3": 390}

# myvar = pd.Series(calories)
# print("Series from dict:", myvar)

# ########################################

# Series using only data from sepcific keys
# calories = {"day1": 420, "day2": 380, "day3": 390}

# myvar = pd.Series(calories, index = ["day1", "day2"])
# print("Series from specific dict. keys", myvar)

# ########################################

# Data Frames: multi-dimensional tables

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

myvar = pd.DataFrame(data)
print("Data Frame from given data:", myvar)

