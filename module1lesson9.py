# Safeguarding Your Code - Python Exception Handling

''' What are Errors and Exceptions?
        Definition:
            Syntax errors occure when the Pythong interpreter encounters a statement that breaks the rules 
            of the language syntax.
            Exceptions are errors detected during execution.
            
            Common Exception Types:
                ZeroDivisionError :     Trying to divide by zero.
                TypeError:              An operation or funtion is applied to an object of inappropriate type.
                ValueError:             A function receives an argument of the right type but inappropriate value.
                
                ex Syntax Error:
                if True
                    print("Hello")              # Missing colon at the end of if statement
                
                ex Runtime Exception:
                x = 1/0                         # This will raise ZeroDivisionError            '''


# Basic Exception Handling with "try" and "except"

''' Basic Syntax:
        try:
            # Code that may raise an exception
        except ExceptionType:
            # Code that runs if an exception occurs'''

try:                                                                        # ERROR EXAMPLE
    x = 10/0
except ZeroDivisionError:
    print("You can't divide by zero!")
    
    
# Exercise 9.1

try:
    first_number = int(input("Please provide your first number: "))
    second_number = int(input("Please provide your second number: "))
    result = first_number / second_number

except ValueError:
    print("Please make sure to enter a valid whole number")

except ZeroDivisionError:
    if second_number == 0:
        print("You cannot divide by zero!")

print(result)


# "else" and "finally" Clauses
    ''' The "else" block is executed if no exceptions occur in the "try" block.
        The "finally" block is executed no matter what, regardless of whether an exception occured."'''
        
try:                                                        # "else" amd "fainlly" example
    x = int(input("Enter a number: "))
    result = 10 / x
except (ValueError, ZeroDivisionError) as e:
    print(f"An error occurred: {e}")
else:
    print(f"The result is {result}")
finally:
    print("Execution complete!")


# Best Practices for Exception Handling

''' -Catch specific exceptions rather than a generic "except".
    
    -Only use exceptions for erro handling, not for regular control flow.
    
    -Avoid swallowing exceptions silently without logging or taking action.'''


# Exercise 9.2

try:
    x = int(input("How much would you like to withdraw? "))
    account_balance = 1500
    result = account_balance - x
except ValueError:
    print("Please make sure to enter a valid whole number")
    
except ValueError:
    if x <= 0:
        print("Please make sure to enter a valid whole number")
    
except ZeroDivisionError:
    if x > account_balance:
        print("Your withdrawl request exceeds your account balance. Please enter a lower amount.")
        
else:
    print(f"Your account balance is {result}.")

finally:
    print("Thank you and have a great day!")
    
    