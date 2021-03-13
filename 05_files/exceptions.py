try:
    number = int(input("? "))
    print(10 / number)
except ValueError:
    print("Not a valid integer")
except ZeroDivisionError:
    print("Can't divide by zero")
except:
    print("Some other exception happened")
print("Finished")

valid_input = False
while not valid_input:
    try:
        age = int(input("Age: "))
        valid_input = True
    except ValueError:
        print("Invalid (not an integer)")
print("Next year you will be", age + 1)

valid_age = False
while not valid_age:
    try:
        age = int(input("Age: "))
        if age < 0:
            print("Invalid age - must be non-negative")
        else:
            valid_age = True
    except ValueError:
        print("Invalid age - enter a number")
print("You are {} years old".format(age))
