# Working with Python integers
"""There are two ways to divide:
    print(x/y) this may return a float(number w/decimals)
    print(x//y) this will return an integer from a rounded float"""
    
milk_cost = 5
eggs_cost = 3
coffee_cost = 10
total_cost = milk_cost + eggs_cost + coffee_cost
print(f"The Total Cost: ${total_cost:.2f}")
total_discount = .1
discounted_total = total_cost * total_discount
discounted_cost = total_cost - discounted_total
print(f"The final discounted cost is: ${discounted_cost:.2f}")


# Power operator (**)

print(2**3)

# Power operator alternative pow()

print(pow(2,3))


# Common integer functions
# abs() - absolute value of an integer
print(abs(-10))

# round() - rounds a float up/down as applicable
print(round(3.14))
print(round(3.56))

# Type conversion - converting strings to integers

num_str = "123"
num = int(num_str)
print(num + 1)


# Final Exercise

first_number = input("Give me a number: ")
second_number = input("Give me a second number: ")
print(f"The numbers you gave me are {first_number} and {second_number}")
first_number = int(first_number)
second_number = int(second_number)
sum = first_number + second_number
print(f"The sum of your numbers is: {sum}")
difference = first_number - second_number
print(f"The difference of your numbers is: {difference}")
product = first_number * second_number
print(f"The product of your numbers is: {product}")
quotient = first_number / second_number
print(f"The quotient of your numbers is: {quotient}")