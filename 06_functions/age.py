"""
Write a program that asks the user for their age and then prints whether it is odd or even.
The program should not crash if the user enters a non-number 
The program should not allow an invalid age number
Re-prompt until a valid number is entered
"""

# my answer
MAX_AGE = 150
MIN_AGE = 0

# valid_age = False
# while not valid_age:
#     try:
#         age = int(input("Enter age: "))
#         while not MIN_AGE <= age <= MAX_AGE:
#             print("Please enter a valid age number ({}-{})".format(MIN_AGE, MAX_AGE))
#             age = int(input("Enter age: "))
#         valid_age = True
#     except ValueError:
#         print("Invalid age - enter a valid number")
# if age % 2 == 0:
#     print("Your age is even")
# else:
#     print("Your age is odd")

# solution provided
def main():
    age = 0
    valid_age = False
    while not valid_age:
        try:
            age = int(input("Enter age: "))
            while not MIN_AGE <= age <= MAX_AGE:
                print("Please enter a valid age number ({}-{})".format(MIN_AGE, MAX_AGE))
                age = int(input("Enter age: "))
            valid_age = True
        except ValueError:
            print("Invalid age - enter a valid number")
    if is_even(age):
        print("Your age {} is even".format(age))
    else:
        print("Your age {} is odd".format(age))

def is_even(number):
    return number % 2 == 0


main()
