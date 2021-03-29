PRODUCTS_FILE = "products.csv"
MENU_STRING = ">>>"


def main():
    products = load_products()
    print(products)
    print(MENU_STRING)
    choice = input(">").upper()
    while choice != "Q":
        if choice == "L":
            list_products(products)
        elif choice == "S":
            swap_sale_status(products)
        else:
            print("Invalid")

        print(MENU_STRING)
        choice = input(">").upper()
    save_products(products)
    print("Finished")


def load_products():
    print("loading")
    products = [["Phone", 340, False], ["PC", 1420.95, True], ["Plant", 24.5, True]]
    return products


def list_products(products):
    print("list")
    for product in products:
        print(product)


def swap_sale_status(products):
    list_products(products)
    is_valid_input = False
    while not is_valid_input:
        try:
            number = int(input("? "))
            if number < 0:
                print("Product must be >= 0")
            else:
                is_valid_input = True
        except ValueError:
            print("Invalid (not an integer)")
    print(products[number])


main()
