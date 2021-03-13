name = 'John Marwood Cleese'
first, middle, last = name.split()
transformed = last + ', ' + first + ' ' + middle
print(name.split())
print(transformed)
print(name)
print(first)
print(middle)

phone = "07-47811234"
print(phone.split('-'))
print(phone.split('-')[0])  # 07
print(phone.split('-')[1])  # 47811234