"""CP1404 Week 09 Pracs
Unreliable Car Class
Estimate: 25 minutes
Commenced: 10:34am
Complete: """

from car import Car
from random import randint


class UnreliableCar(Car):

    def __init__(self, reliability: int, **kwargs):
        super().__init__(**kwargs)
        self.reliability = reliability

    def drive(self, distance):
        random_breakdown_modifier = randint(1, 100)
        if random_breakdown_modifier < self.reliability:
            distance_driven = super().drive(distance)
            return distance_driven
        return 0
