# comments = just practicing comments from live session instruction
''' you can also do
multiline comments for a more lengthy explanation of code/context
that is going to span more than one line'''

name = "John"
greeting = 'Hello!'

multi_line = '''This is a
multi-line string.'''
print(multi_line)

word = "Python"
print(word[0])
print(word[2])

first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name
print(full_name)

exclamation = "Wow! " *3
print(exclamation)

name = "Python"
print(len(name))

language = "Python"
print(language[0:3])
print(language[3:])
print(language[-1])

message = "Hello World!"
print(message.upper())
print(message.lower())

text = " Python "
print(text.strip())

message = "Hello, World!"
print(message.replace("World", "Python"))

sentence = "Python is fun"
words = sentence.split()
print(words)

words = ['Python', 'is', 'fun']
sentence = " ".join(words)
print(sentence)

filename = "report.pdf"
print(filename.endswith(".pdf"))

message = "I am hungry!"
print(message.upper())

message = " I am hungry!   "
print(message.strip())

message = "I am hungry!"
print(message.replace("hungry", "tired"))

sentence = "I am hungry!"
words = sentence.split()
print(words)

name = "John"
age = 30
print("My name is {} and I am {} years old.".format(name, age))

name = "John"
age = 30
print(f"My name is {name} and I am {age} years old.")

text = "hello"
text[0] = "H"
print(text)

text = "hello"
text = "H" +text[1:]
print(text)

result = ""
result += "a"
print(result)

result = result +"a"
print(result)

# Return a random element from a list:
import random

first_names = ["Christian", "Dylan", "Travis", "Katelyn"]
last_names = ["Sachs", "Katina", "Peck", "Mehner"]

f_name = random.choice(first_names)
l_name = random.choice(last_names)
print(f_name + ' ' + l_name)

# or can do f-string
import random

first_names = ["Christian", "Dylan", "Travis", "Katelyn"]
last_names = ["Sachs", "Katina", "Peck", "Mehner"]

f_name = random.choice(first_names)
l_name = random.choice(last_names)
print(f'{f_name} {l_name}')
