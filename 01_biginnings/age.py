"""
01-Beginnings
Write pseudocode for a program that asks the user for their age and
continues to do so until they enter a valid age (0 to 150)
The program should then display the user's age
"""

MAX_AGE = 150
MIN_AGE = 0

age = int(input("Enter age: "))
while age < MIN_AGE or age > MAX_AGE:
    print("Please enter an age ({}-{})".format(MIN_AGE, MAX_AGE))
    age = int(input("Enter age: "))
print("You age is {}.".format(age))

if age % 2 == 0:
    print("Your age is even")
else:
    print("Your age is odd")

age = int(input("Enter age: "))
while age < MIN_AGE or age > MAX_AGE:
    print("Please enter an age ({}-{})".format(MIN_AGE, MAX_AGE))
    age = int(input("Enter age: "))

if age >= 20:
    print("You are an adult")
else:
    print("You are a child")
