# Write a function count(filename) that takes a filename as argument and containing the count of big words and small words (words that are greater than 6 characters in returns
# a dictionary length are big words and others are small words). The Close the file after use. Check for exceptions as well.
# Format of dictionary returned : {‘big’: 3, ‘small’: 4}

def count(filename):
    dict1={'big':0,'small':0}
    # write function body
    file = open(filename, "r")
    
    data = file.read()
    element_list = data.split(" ")
    
    for i in element_list : 
        c1 = 0
        for j in i :
            c1 += 1
        if c1 > 6 : 
            dict1['big'] = dict1['big'] + 1
        else : 
            dict1['small'] = dict1['small'] + 1
    file.close()        
    return dict1
