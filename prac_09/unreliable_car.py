from car import Car
from random import randint


class UnreliableCar(Car):
    """Specialised version of a Car that includes a reliability attribute."""

    def __init__(self, name, fuel, reliability):
        """Initialise a Taxi instance, based on parent class Car."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def __str__(self):
        """Return a string like a Car but with reliability attribute."""
        return f"{super().__str__()}, reliability = {self.reliability}"

    def drive(self, distance):
        """Drive the car a given distance if random_number generated is less than car's reliability"""
        random_number = randint(0, 100)
        if random_number >= self.reliability:
            distance = 0
        distance_driven = super().drive(distance)
        return distance_driven
