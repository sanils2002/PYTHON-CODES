# Write a function count(filename) that takes a filename as argument and returns the count of words such that the length of the word is less than equal to 3 and contains
# atleast two vowels. Check for exceptions as well.
# For example, “too”,”are”,”eat” etc.

def count(filename):
    
    vowels = ['a', 'e', 'i', 'o', 'u']
    file = open(filename, "r")
    
    filestuff = file.read()
    filestuff = filestuff.lower()
    filestuff = filestuff.split(" ")
    result = 0

    for x in filestuff : 
        counter = 0
        voCtr = 0
        for y in x :
            counter += 1
        if counter <= 3 : 
            for y in x: 
                if y in vowels :
                    voCtr += 1
            if voCtr >= 2:
                result += 1


    file.close()
    return result
