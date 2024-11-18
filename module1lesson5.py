<<<<<<< HEAD
# Conditional Logic in Python

''' Conditional Statemenets:
if: used to test if a condition is true
elif: (short for "else if") checks for multiple conditions. You can have as many elif's in your conditional statements
else: executes if none of the conditions above are true'''

# Python Conditional Statement Syntax

if condition:
    # code to execute if condition is True
elif another_condition:
    # code to execute if another_condition is True
else:
    # code to execute if all conditions are False


#EXAMPLE

x = -10

if x > 0:
    print("x is positive")
elif x == 0:
    print("x is zero")
else:
    print("x is negative")
 
    

# Comparison Operators
#   == : Equal to
#   != : Not equal to
#   >  : Great than
#   <  : Less than
#   >= : Greater than or equal to
#   <= : Less than or equal to

#Logical Operators
#   and : True if both conditions are true
#   or  : True if at least one condition is true
#   not : True if the condition is false


# EXAMPLE

age = 25
is_student = True

if age >= 18 and is_student:
    print("Eligible for a student discount.")
else:
    print("Not eligibile for a student discount.")



# Final Exercise

import random
random_int = random.randint(1, 10)
print(random_int)
guess_one = input("Try to guess the secret number: ")
guess_one = int(guess_one)
if guess_one == random_int:
    print("Well done! You guessed it on the first try!")
elif guess_one < random_int:
    print("Too low! Try again!")
else:
    print("Too high! Try again!")
    
=======
# Conditional Logic in Python

''' Conditional Statemenets:
if: used to test if a condition is true
elif: (short for "else if") checks for multiple conditions. You can have as many elif's in your conditional statements
else: executes if none of the conditions above are true'''

# Python Conditional Statement Syntax

if condition:
    # code to execute if condition is True
elif another_condition:
    # code to execute if another_condition is True
else:
    # code to execute if all conditions are False

#EX

x = -10

if x > 0:
    print("x is positive")
elif x == 0:
    print("x is zero")
else:
    print("x is negative")
    

# Comparison Operators
#   == : Equal to
#   != : Not equal to
#   >  : Great than
#   <  : Less than
#   >= : Greater than or equal to
#   <= : Less than or equal to

#Logical Operators
#   and : True if both conditions are true
#   or  : True if at least one condition is true
#   not : True if the condition is false

>>>>>>> 28752bdd980861376f59568409b6d01a610311ed
