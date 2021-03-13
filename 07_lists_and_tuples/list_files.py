
input_file = open("subjects.txt")
subjects = input_file.readlines()
input_file.close()

subjects = [subject.strip() for subject in subjects]  # strip() removes \n  # list comprehension
print(subjects)

# for subject in subjects:
#     if subject[2] == '1':
#         print(subject)

# now use 'list comprehension'
first_year_subjects = [subject for subject in subjects if subject[2] == '1']
print(first_year_subjects)