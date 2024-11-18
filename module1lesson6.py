# Power of lists in Python
# Lists are defined by square brackets [] abd cab cibtaub utens if different data types, including integers, floats, strings, Booleans or even other lists.
# my_list = [1, 2, 3, 4, 5]
# mixed_list = [1, "apple", 3.14, True]
"""Key characteristics of lists
    Order: Items have a specific order.
    Indexing: Items in a list are indexed starting from 0."""

my_list = ["apple", "banana", "cherry"]
print(my_list[0])
print(my_list[-1])


# Modifying List
"""Add an item: .append(item) adds an item to the end.
    my_list.append("orange")

    Insert at a specific index: .insert(index, item) adds an item at the specified position.
     my_list.insert(1, "blueberry")
     
    Remove an item: .remove(item) removes the first matching item.
     my_list.remove("apple")
    
    Delete by index: Use del keyword or .pop() to remove an item at a specfic index.
     del my_list[0]   delete the fisrt item
     my_list.pop(1)   remove and returns the item at index 1"""
     

# Slicing lists - slicing allows us to access a subset of items in a list.
# my_list = [1, 2, 3, 4, 5, 6]
# subset = my_list[1:4]
# returns [2, 3, 4]

# Omit the start or end index to slice from the beginning or to the end.
# print(my_list[:3])    returns [1, 2, 3]
# print(my_list[3:])    returns [4, 5, 6]



# Exercise 6.1

fruits = ["apple", "banana", "cherry", "date"]
print(fruits[0])
print(fruits[-1])
fruits.append("elderberry")
fruits.insert(0, "blueberry")
print(fruits)
fruits.remove("banana")
del fruits[0]
print(fruits)
citrus_fruits = fruits[1:3]
print(citrus_fruits)




# List Functions and Methods

""" Built-in Functions:
    len(): returns the number of items in a list.
        len([1, 2, 3, 4])   returns 4
    min() / max(): returns the smallest/largest item.
        min([5, 3, 8])   returns 3
        max([5, 3, 8])  returns 8
    
    Common List Methods:
    .sort(): sorts the list in place
        numbers = [4, 1, 7, 3]
        numbers.sort()  returns [1, 3, 4, 7]
        
    .reverse(): reverse the items in the list
        numbers.revers()    returns [7, 4, 3, 1]
        
    .extend(): adds all items from one list to another
        list1 = [1, 2, 3]
        list2 = [4, 5']
        list1.extend(list2) returns [1, 2, 3, 4, 5]
        
        NOTE - you can alsot concatenate lists together.   list1 + list2  """

# Nested Lists - A list can contain other lists as its elements, forming a matrix-like structure.
#   matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#   print(matrix[0][1])     returns 2


# Exercise 6.2


books = []
book_1 = input("Please enter your most favorite book: " "")
book_2 = input("Please enter your second most favorite book: " "")
book_3 = input("Please enter your  third most favorite book: " "")
books.insert(0, book_1)
books.insert(1, book_2)
books.insert(2, book_3)
books.sort()
print(books)