# Function Mastery in Python

'''Key Concepts:
    What is a funtion?
        A block of organized, reusable code.
    Why use funtions?
        To avoid code duplication, improve readability, and make debugginh easier.'''
        

# Defining and Calling Functions

'''Defining a fucntion:  Use the "def" keyword, followed by the function name and parentheses.
   Calling a funtion:    To utilize/run the funtion, use its name followed by parenthese. "funtion()" 
   
   
   Paramentes and Arguments
    Parameters:  Variables defined in the funtion declaration.
    Arguments:   Values passed into the function when it is called.'''
    
    
# Exercise 8.1
    
def introduce_yourself(name, hobby):
        print(f"Hello, {name}! I heard your favorite hobby is {hobby}!") 
    
introduce_yourself('Mikey', 'tennis')


# Return Statements - useful when you want to get an output from a function and use it later.

def add_numbers(a, b):
    return a + b

result = add_numbers(5,3)
print(result)


# Function Scope (Local vs Global Variables)
''' Local variables:    Variables defined inside a function, only accessible within that funtion.
    Global variables:   Variables defined outside any function and accessible throughout the code.'''
    
x = 10      # Global Variable

def print_number():
    x = 5       # Local Variable
    print(x)    # Output: 5  

print_number()
print(x)        # Output: 10


# Default Parameters & Variable-Length Arguments

''' Default parameters: Functions can have defualt values for parametes, which are uysed if no arguments is provided.'''

def greet(name="Student"):
    print(f"Hello, {name}!")
    
greet()             # Output: Hello, Student!
greet("Alice")      # Output: Hello, Alice!


''' Variable-Length Arguments: Use *args and **kwargs to pass a variable number of arguments to a funtion.'''

def add_numbers(*args):
    return sum(args)
    
print(add_numbers(1, 2, 3))     # Output: 6
print(add_numbers(5, 10))       # Output: 15



# Exercise 8.2

def squared_numbers(numbers, exponent):
    result = []
    for num in numbers:
        result.append(num ** exponent)
    return result

numbers = [3, 99, 12, 1, 7]
exponent = 2

exponents = squared_numbers(numbers, exponent)
print(exponents)

