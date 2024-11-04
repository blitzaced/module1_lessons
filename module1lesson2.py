name = input("What is your name?")
print(f"Hello, {name}!")

favorite_color = input("What is your favorite color?")
print(f"Your favorite color is {favorite_color}!")

age = input("How old are you?")
print(f"I can't believe you are {age} years old!")

print("Please meet " + name + "! Their favorite color is " + favorite_color + ", and they are " + age + " years old!")




exam_score = int(input("Enter your exam score: "))

if exam_score > 90:
    print("Your exam score is excellent!")
elif exam_score > 69 and exam_score < 90:
    print("Your exam score is good!")
else:
    print("Your exam score needs improvement!")
    