# VARIABLE NAME
# A variable can have a short name (like x and y) or a more descriptive name (age, carname, total_volume). Rules for Python variables:
# A variable name must start with a letter or the underscore character
# A variable name cannot start with a number
# A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
# Variable names are case-sensitive (age, Age and AGE are three different variables)
str1 = "IIITN"
str_var = "IIITN"
_str_var = "IIITN"
myStr = "IIITN"
MYSTR = "IIITN"
mystr2 = "IIITN"
#---------------------------------------------------------------------------------------------------------------------------------------------
#CASE SENSITIVITY
#A will not overwrite a
a = 12
A = "IIITN"
print("a=",a, "A=", A)
#---------------------------------------------------------------------------------------------------------------------------------------------
# DIFFERENT WAYS OF INITIALIZING VARIABLE
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

x = y = z = "Orange"
print(x)
print(y)
print(z)
#---------------------------------------------------------------------------------------------------------------------------------------------
# DELETING A VARIABLE
del x
del y, z
#print(x)
# #---------------------------------------------------------------------------------------------------------------------------------------------
# STRINGS
str1 = "Hello World!"

print(str1)          # Prints complete string
print(str1[0])       # Prints first character of the string
print(str1[2:5])     # Prints characters starting from 3rd to 5th
print(str1[2:])      # Prints string starting from 3rd character
print(str1 * 2)      # Prints string two times
print(str1 + "TEST") # Prints concatenated string
# #---------------------------------------------------------------------------------------------------------------------------------------------
#LISTS

data = [ 'abcd', 786 , 2.23, 'xyz', 70.2 ]
data1 = [123, 43.9]

print(data)          # Prints complete list
print(data[0])       # Prints first element of the list
print(data[1:3])     # Prints elements starting from 2nd till 3rd 
print(data[2:])      # Prints elements starting from 3rd element
print(data * 2)      # Prints list two times
print(data + data1)  # Prints concatenated lists

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

# #---------------------------------------------------------------------------------------------------------------------------------------------
# TUPLES
# Tuples are enclosed in parentheses ( ( ) ) and cannot be updated.

data_tuple = ( 'abcd', 786 , 2.23, 'xyz', 70.2  )
data1_tuple = (123, 43.9)

print(data_tuple)                # Prints the complete tuple
print(data_tuple[0])             # Prints first element of the tuple
print(data_tuple[1:3])           # Prints elements of the tuple starting from 2nd till 3rd 
print(data_tuple[2:])            # Prints elements of the tuple starting from 3rd element
print(data1_tuple * 2)           # Prints the contents of the tuple twice
print(data_tuple + data1_tuple)  # Prints concatenated tuples

data1[1]= 'hello'
#data1_tuple[1]='hello'          # Cannot be changed

print(data1)
print(data1_tuple)
# #---------------------------------------------------------------------------------------------------------------------------------------------
# Dictionary

stud_dict1 = {}
stud_dict1['roll_no1']= 8.6
stud_dict1[2]=5.9

stud_dict = {'college_name': 'IIITN','stud_name':'abc', 'dept': 'cse', 'stud':'abc'}
print(stud_dict)

# print(stud_dict1['roll_no1'])       # Prints value for 'one' key
# print(stud_dict1[2])           # Prints value for 2 key
# print(stud_dict1)       # Prints complete dictionary
# print(stud_dict.keys())   # Prints all the keys
# print(stud_dict.values()) # Prints all the values

# #--------------------------------------------------------------------------------------------------------------------------------------------
# SET
set1 = {"abc", 34, True, 40, "male"}

print(set1)
#print(set1[0])          # set is not indexed

#input set
set1 = {4, 6, 12, 11, 3, 5}

#Access element using for loop
print("\nReading elements of the set: ")

for x in set1:
      print(x)

set1 = {"apple", "mango", "cherry", "pear", "guava"}

#check for an element
print("apple" in set1)
print("watermelon" in set1)

# #--------------------------------------------------------------------------------------------------------------------------------------------
# # CONDITIONS AND IF..ELSE

# # Equals: a == b
# # Not Equals: a != b
# # Less than: a < b
# # Less than or equal to: a <= b
# # Greater than: a > b
# # Greater than or equal to: a >= b

# a = 200
# b = 33
# c = 500
# if a > b or a > c:
#   print("At least one of the conditions is True")


# a = 200
# b = 33
# c = 500
# if a > b and c > a:
#   print("Both conditions are True")

# a = 200
# b = 33
# c = 500
# if not a > b:
#   print("Not True")
