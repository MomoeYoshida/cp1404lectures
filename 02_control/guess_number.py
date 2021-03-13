"""
Write the program asking the user to guess a number between 1 and 10
and keep asking until they get it right.
Use a CONSTANT for the secret number
Just use "?" as the prompt for now
"""
SECRET = 6
guess = int(input("? "))
while guess != SECRET:
    print("Guess again!")
    guess = int(input("? "))
print("You got it!")
