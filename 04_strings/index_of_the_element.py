"""
04-Strings
"""
hello_str = 'Hello World'
print(hello_str[1])
print(hello_str[-1])
# print(hello_str[11])
print(hello_str[6:10])  # the last index is one after what is included
print(hello_str[6:])
print(hello_str[:5])
print(hello_str[3:-2])
print(hello_str[0:11:2])

print("bobby"[0].isupper())
print("Bobby"[0].isupper())

subject = '16-CP1404-TSV-SP1'
print('CP' in subject)
print('16' == subject[:2])