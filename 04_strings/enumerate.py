_author_ = 'Momoe Yoshida'

for i, char in enumerate(_author_):
    print(i, char)

# better line-up
for i, char in enumerate(_author_):
    print("{:2} - {}".format(i, char))
