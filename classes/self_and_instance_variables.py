"""self is used to create instance variables instead of local variables"""


def drive(self, distance):
    """Drive the car a given distance if it has enough fuel."""
    if distance > self.fuel:
        distance = self.fuel
        self.fuel = 0
    else:
        self.fuel -= distance
    self.odometer += distance
    return distance

# distance is a local variable, so it only exists in this function
# self.fuel is an instance variable, available anywhere in the class
