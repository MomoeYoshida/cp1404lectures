"""
05-Files and Exceptions
"""
# open file for writing (creates file if it does not exist) overwrites file if it exists (you can use the print
# command to write to it by adding the keyword argument like file=temp_file)
temp_file = open("temp.txt", "w")
print("first line", file=temp_file)
print("second line", file=temp_file)
temp_file.close()

# write to a file
word_list = ['First', 'Second', 'Third', 'Fourth']
out_file = open('outFile.txt', 'w')
for word in word_list:
    out_file.write(word + ' line\n')
out_file.close()

in_file = open("textfile.txt", "r")
text = in_file.readline()
print(text)
for line in in_file:
    print("* ", repr(line))
in_file.close()

out_file = open("textfile.txt", "a")
print("96", file=out_file, end='')
out_file.write("23")
out_file.close()
