print("Sorry, is this the {} minute {}?".format(5, 'ARGUMENT'))

# string 10 spaces wide including the object, right justified
# decimal 10 spaces wide including the object, left justified
print('{:>10s} is {:<10d} years old'.format('Bill', 25))

# decimal 10 and 4 spaces wide including the object
for i in range(5):
    print("{:10d} --> {:4d}".format(i, i ** 2))

from math import *
print(pi)
print("Pi is {:.4f}".format(pi))  # floating-point precision 4
print("Pi is {:8.4f}".format(pi))  # 8 spaces wide including the object and precision 4
print("Pi is {:8.2f}".format(pi))  # 8 spaces wide including the object and precision 2

name = "Monty"
money = 73.6
print("Output: {} has ${:.2f}".format(name, money))

print('{0} is {2} and {0} is also {1}'.format('Bill', 25, 'tall'))

for n in range(3, 11):
    print('{:4}-sides:{:6}{:10.2f}{:10.2f}'.format(n, 180*(n-2), 180*(n-2)/n, 360/n))

print("here: {:^8}.".format("a"))  # at the center
