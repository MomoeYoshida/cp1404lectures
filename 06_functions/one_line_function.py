"""
Write a one-line function that determines if someone is
an adult based on their age, passed in.
What type will it return?
What is a good format for the name?
"""

def is_adult(age):
    return age >= 18

print("Got {}, expected True".format(is_adult(18)))
print("Got {}, expected False".format(is_adult(17)))
assert is_adult(20)
assert not is_adult(0)
