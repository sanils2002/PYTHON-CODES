# There are N numbers in a list which is passed as argument to the function. Write a function findSquare(list) that calculates the square of only those numbers in the list
# whose least significant digit is 5. Store the number and its square in a dictionary and return the dictionary.

def findSquare(list):
    dict1={}  # This variable should store the number and its square in a dictionary 
    # write function body
    i=0
    for x in list:
        if x%5==0 and x%10!=0:
            dict1[x] = x*x
            i = i+1
        else:
            continue
    return dict1
