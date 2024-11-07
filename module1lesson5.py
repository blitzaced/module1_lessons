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

