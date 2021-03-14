"""Do this now:
Write a function to get a valid age from a user
Write two lines of main code to show its use
"""
# my answer
MINIMUM_AGE = 0
MAXIMUM_AGE = 150


def main():
    """Get and print user's age using functions."""
    age = int(input("Enter your age (0-150): "))
    while not MINIMUM_AGE <= age <= MAXIMUM_AGE:
        print("Invalid age!")
        age = int(input("Enter your age (0-150): "))
    print("Your age is {}.".format(age))


main()


# suggested solution


def main():
    age = get_valid_age()
    print("Your age is {}.".format(age))


def get_valid_age():
    age = int(input("Enter your age (0-150): "))
    while not MINIMUM_AGE <= age <= MAXIMUM_AGE:
        print("Invalid age!")
        age = int(input("Enter your age (0-150): "))
    return age


main()

