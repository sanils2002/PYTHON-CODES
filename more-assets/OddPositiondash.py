# Given a list of length N (be even no.) which contains name and age of N/2 people. Name and age of a person are the adjacent elements in the list which passed as argument
# to the function. Write a function concat(list) that creates a new list from the first list by concatenating the name and age of each person. The function should return this new list.
# For example, [‘Meera’,43] is the item in first list, the new list will contain [‘Meera-43’]. Write a python program to accomplish the same.

def concat(list):
    newlist=[]   # this is the newlist that the function sholud return
    # write function body
    n=len(list)
    i=0
    while(i<n):
        newlist.append(list[i]+'-'+str(list[i+1]))
        i=i+2
    return newlist
