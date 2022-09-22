# Purpose: This is a basic implementation of a linked list for fun and just offers 
# a playground to manipulate linked lists
# Author: Edwin
# Date: September 2022

# The linked List class
from heapq import heapify
class MyLL:
    # COnstructor
    def __init__(self, val=None, next=None) -> None:
        self.val = val
        self.next = next
    
        
a = MyLL(2)

# Insert more values
arr_to_insert = [10, 3, 4, 1, 9, 3, 8]

temp = a
while(temp.next != None):
    temp = temp.next

for i in range(len(arr_to_insert)):
    temp.next = MyLL(arr_to_insert[i])
    temp = temp.next

# Print the sample list created
temp = a
while(temp != None):
    print(temp.val)
    temp = temp.next

# Implement heap on the list as a beginning stage of a heap sort
arr = []
temp = a
while(temp != None):
    arr.append(temp.val)
    temp = temp.next

heapify(arr)
print(arr)

print("edwin")
