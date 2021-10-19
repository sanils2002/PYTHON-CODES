# READING FILE

f = open("D:\\IIITN\\Python\\demoFile.txt", "r")
#print(f.read())
#print(f.read(5))

#print(f.readline())
#print(f.readline())
# contents = f.readlines()
# print(type(contents))
# print(contents)


# for x in f:
#   print(x)           # Reads 1 line at a time
  
# f.close()
#--------------------------------------------------------------------------------------------------------------------------------------------------------------

# APPENDING FILE
# f = open("D:\\IIITN\\Python\\demoFile2.txt", "a")
# f.write("Nagpur is named after the Great river Nag which flows through the city.")
# f.close()

# #open and read the file after the appending:
# f = open("D:\\IIITN\\Python\\demoFile2.txt", "r")
# print(f.read())

# f.close()
#-----------------------------------------------------------------------------------------------------------------------------------------------

# WRITING TO A FILE
# f = open("D:\\IIITN\\Python\\demoFile3.txt", "w")
# f.write("CONTENTS ARE DELETED !!!")
# f.close()

# #open and read the file after the appending:
# f = open("D:\\IIITN\\Python\\demoFile3.txt", "r")
# print(f.read())

# # FILE ATTRIBUTES
# # if not(f.closed) :         # Returns true if file is closed
# #     print("File is not closed. Kindly Close the file")

# # print("The mode in which file is open:", f.mode)     # returns the file mode

# # print("The name of the file is:", f.name)           # returns filename

# SOME MORE FUNCTIONS
# f = open("D:\\IIITN\\Python\\demoFile.txt", "r")
# print(f.read())
# f.flush() # Flushes the internal buffer memory
# print(f.fileno)   # Prints the internal file discriptor
# f.close()
# f = open("D:\\IIITN\\Python\\demoFile.txt", "r")
# # print(f.read())
# # print(f.tell())


# print(f.readline())
# print(f.tell())
# #f.seek(0)
# print(f.readline())
# f.close()


#------------------------------------------------------------------------------------------------------------------------------------------------

# DELETING A FILE
import os
os.remove("D:\\IIITN\\Python\\demoFile3.txt")
print("File is deleted!!!")