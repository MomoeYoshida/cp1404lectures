"""
Write pseudocode and Python for a program that opens a file and toggles "on" and "off"
each time it's run. So, if the file contains "on", change it to "off" and vice versa

open file for reading
read line from file
close file
if line == "on"
    line = "off"
else
    line = "on"
open file for writing
write line to file
close file
"""

try:
    in_file = open("on_off.txt", 'r')
    line = in_file.read()
    in_file.close()
    if line == "on":
        line = "off"
    else:
        line = "on"
    out_file = open("on_off.txt", 'w')
    print(line, file=out_file)
    out_file.close()
except FileNotFoundError:
    print("Error with file; aborting!")

