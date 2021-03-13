PRICE_PER_M = 3.5

length = float(input("Length: "))
width = float(input("Width: "))
area = length * width
cost = area * PRICE_PER_M
print("For", area, "m2 that will cost", cost)

choice = input("> ").upper()
if choice == "A":
    do_something()
elif choice == "B":
    do_something_else()
elif choice == "C":
    do_another_something()