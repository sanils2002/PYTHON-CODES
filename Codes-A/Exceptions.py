# EXCEPTION HANDLING
# Built-in exceptions are : ImportError, IndexError, MemoryError, NameError, OverflowError, ZeroDivisionError, IOError


# try...except....else.....finally

# IOError exception, if file is not present
# try:
#     f = open ("D:\\IIITN\\Python\\demoFile4.txt", "r")
#     f.readline()
# except IOError:
#     print("Error in opening or reading file")
# else :
#     print("Successful")

#     f.close()
#--------------------------------------------------------------------------------------------------------------------------------------
# EXCEPT WITHOUT EXCEPTION

# while True:
#     b = 1
#     try:
#         a = int (input("Enter an integer:"))
#         b = 24 / a
#         break
#     except:
#         print("Enter a Positive Number")
# print("Answer = ", b)

# --------------------------------------------------------------------------------------------------------------------------------------

# USE OF FINALLY
# try:
#     f = open ("D:\\IIITN\\Python\\demoFile4.txt", "r")
#     f.readline()
# except IOError:
#     print("Error in opening or reading file")
# else :
#     print("Successful")
# finally:
#     f.close()
#     print("File Closed")

#---------------------------------------------------------------------------------------------------------------------------------------

# USER DEFINED EXCEPTION

class NegativeNum(Exception):
    msg = "Negative Number"
try:
    n = int(input("Enter an positive integer:"))
    if n < 0:
        raise NegativeNum
    else:
        print("The number you have entered is:", n)
except NegativeNum as Err:
    print(Err.msg)


