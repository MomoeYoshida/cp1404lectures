"""
02 - Control
"""

age = int(input("Age: "))
while age < 0:
    print("Invalid age")
    age = int(input("Age: "))

if age < 18:
    print("At", age, "you are a minor.")
else:
    print("At", age, "you are an adult.")

number = int(input("Number: "))
while number > 0:
    number_squared = number ** 2
    print("That number {} squared is {}.".format(number, number_squared))
    number = int(input("Number: "))
print("Stop")
