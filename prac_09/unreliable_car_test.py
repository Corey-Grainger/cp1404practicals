"""CP1404 Week 09 Pracs
Unreliable Car Test"""

from unreliable_car import UnreliableCar

bomb = UnreliableCar(20, name="Bomb", fuel=1000)
surprisingly_reliable_car = UnreliableCar(101, name="Japanese Hatch", fuel=1000)
distance_driven = bomb.drive(40)
print(bomb)
print(distance_driven)
distance_driven = bomb.drive(150)
print(bomb)
print(distance_driven)
distance_driven = surprisingly_reliable_car.drive(40)
print(surprisingly_reliable_car)
print(distance_driven)
