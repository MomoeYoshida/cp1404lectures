numerator = int(input("Enter a numerator: "))
denominator = int(input("Enter a denominator: "))
if denominator != 0 and numerator % denominator == 0:
    print("Okay")
else:
    print("Error")
