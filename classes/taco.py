class User:
    def __init__(self, name, score, number_of_tacos=5):
        self.name = name
        self.score = score
        self.number_of_tacos = number_of_tacos

    def __str__(self):
        return "{}, {} points, {} tacos left".format(self.name, self.score, self.number_of_tacos)


u1 = User("Ben", 2, 4)
print(u1)
