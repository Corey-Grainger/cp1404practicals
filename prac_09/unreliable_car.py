"""CP1404 Week 09 Pracs
Unreliable Car Class
Estimate: 25 minutes
Commenced: 10:34am
Complete: 10:52"""

from car import Car
from random import randint


class UnreliableCar(Car):
    """Represent an unreliable car."""

    def __init__(self, reliability: int, **kwargs):
        """Initialise an unreliable car."""
        super().__init__(**kwargs)
        self.reliability = reliability

    def drive(self, distance):
        """Drive an unreliable car if it does not randomly break down."""
        random_breakdown_modifier = randint(1, 100)
        if random_breakdown_modifier < self.reliability:
            distance_driven = super().drive(distance)
            return distance_driven
        return 0
