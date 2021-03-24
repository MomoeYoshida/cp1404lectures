ages_dict = {"Bill": 21, "Jane": 34, "Jack": 56}

print(ages_dict["Bill"])

# get method
print(ages_dict.get("Bob", -1))
ages_dict['Bob'] = ages_dict.get("Bob", 0) + 1
print(ages_dict.get("Bob"))
print(ages_dict)

# Write code to prompt the user for a name and age, add
# these to the dictionary, then display all of the data
# nicely.
name = str(input("Name: "))
age = int(input("Age: "))
ages_dict[name] = age
for name, age in ages_dict.items():
    print("{:<10s} - {:>10d}".format(name, age))

# Dictionary comprehension
ages_dict = {"Bill": 17, "Jane": 34, "Jack": 13}
new_ones = {name: age for name, age in ages_dict.items() if age < 18}
print(new_ones)
