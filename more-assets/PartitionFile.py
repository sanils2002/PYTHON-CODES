# Write a function partition(filename) that divides the file contents into two parts. That is, the function should count the total number of lines in the file and should write first
# count/2 lines in one file and the remaining lines in another file. The function should return last line of the first file as a string. Check for exceptions as well.

def partition(filename):
    s1=""   # This variable should store last line of the first file.
    # write function body

    file = open(filename,"r")
    Counter = 0
    Content = file.read()
    CoList = Content.split("\n")
    
    for i in CoList:
        if i:
            Counter += 1

    file.close()
    if Counter==1:
        return file.read()
    else :
        x=Counter//2
        ct=0
        file = open(filename)
        all_lines = file.readlines()
        s1=all_lines[x-1]
        return s1
