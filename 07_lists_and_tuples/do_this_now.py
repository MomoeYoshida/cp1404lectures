"""
Ask the user for their name
Tell them how many vowels are in their name
Use the string.format() method for the last print
"""
VOWELS = "aeiou"

# name = input("Name: ")
name = "Momoe Yoshida"

count_vowel = 0
for letter in name:
    if letter.lower() in VOWELS:
        count_vowel += 1
# print("Out of {} letters, {} has {} vowels".format(len(name), name, count_vowel))

capitals = [c for c in name if c.isupper()]  # list comprehension
vowels = [c for c in name if c.lower() in VOWELS]
new_name = "".join([c for c in name if c.lower() not in VOWELS])  # new name without any vowels
print(new_name)
# print(capitals)
# print(vowels)
