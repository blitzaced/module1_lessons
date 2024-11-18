# Python Loops: The Power of Repetition

''' Types of loops in Python:

    for loop : iterates over a sequence (e.g., list, tuple, string, or range) 
    and executes a block of code for each item in the sequence.
    
    while loop: keeps executing the code block as long as a specified condition remains True.'''


# for loop example
fruits = ['apple', 'banana', 'cherry']
for fruit in fruits:
    print(fruit)

for i in range(5):
    print(i)


# while loop example
current_number = 1                  
while current_number <= 5:
    print(current_number)
    current_number += 1


# Exercise 7.1

current_number = 1
while current_number <= 20:
    if current_number % 2 == 0:
        print(current_number)
    current_number += 1
    


# Control Flow in Loops

'''break Statement - stops the loop prematurely when a certain condition is met.'''
for i in range(10):
    if i == 5:
        break
    print(i)
    

'''continue Statement - skips the current iteration and moces to the next one.'''
for i in range(5):
    if i == 3:
        continue
    print(i)
    

# Exercise 7.2

for i in range(30):
    if i % 3 == 0:
        continue
    if i == 26:
        break
    print(i)
    