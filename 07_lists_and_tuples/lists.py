"""
Iteration
"""


def main():
    numbers = [1, 2, 8, 3, 12, 40, 0]
    # print(is_negative_here(numbers))
    print(sorted(numbers))
    # numbers.sort()  # sort in numerical order!
    print(numbers)
def is_negative_here(numbers):
    for number in numbers:
        print("checking...")
        if number < 0:
            return True
    return False


main()
