number = int(input("Enter number: "))
while not (number >= 1 and number <= 10):
    print("Error - number is outside the range 1-10")
    number = int(input("Enter number: "))

# more readable
number = int(input("Enter number: "))
while not (1 <= number <= 10):
    print("Error - number is outside the range 1-10")
    number = int(input("Enter number: "))

number = int(input("Enter number: "))
while number < 1 or number > 10:
    print("Error - number is outside the range 1-10")
    number = int(input("Enter number: "))
