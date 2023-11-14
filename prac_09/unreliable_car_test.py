"""CP1404 Week 09 Pracs
Unreliable Car Test"""

from unreliable_car import UnreliableCar

bomb = UnreliableCar(50, name="Bomb", fuel=1000)
distance_driven = bomb.drive(40)
print(bomb)
bomb.drive(150)
print(bomb)
