"""Student class."""


class Student:
    def __init__(self, first_name="", last_name="", student_id=0):
        self.first_name = first_name
        self.last_name = last_name
        self.id = student_id
        self._special = True
        self.__secret = ":)"

    def __str__(self):
        return "{} {} ({})".format(self.first_name, self.last_name, self.id)

    def get_full_name(self):
        return self.first_name + " " + self.last_name


# Simple example class usage (client code)
first_name = input("First name: ")
last_name = input("Last name: ")
student_id = int(input("ID: "))
s1 = Student(first_name, last_name, student_id)
print(s1)
print(s1.first_name, "has ID", s1.id)

if __name__ == '__main__':
    s1 = Student("Momoe", "Yoshida", 123)
    print(s1._special)
    # print(s1.__secret)
    print(s1.__dict__)
    print(s1._Student__secret)
    # print(s1)
    # s2 = Student("Bob", "Marley")
    # s2.party()
    # s1.graduate()
    # print(s1.get_full_name())
    # print(s2.get_full_name())
    # s1.first_name
