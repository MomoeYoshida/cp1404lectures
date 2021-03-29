PRODUCTS_FILE = "products.csv"
MENU_STRING = ">>>"


def main():
    print(MENU_STRING)
    choice = input(">").upper()
    while choice != "Q":
        if choice == "L":
            print("list")
        elif choice == "S":
            print("swap")
        else:
            print("Invalid")

        print(MENU_STRING)
        choice = input(">").upper()
    print("Finished")


main()
