"""
CP1404/CP5632 Practical - Client code to use the Car class.
Note that the import has a folder (module) in it.
This is why we name our folders with no spaces or capitals, as valid module names.
"""

from prac_06.car import Car


def main():
    """Demo test code to show how to use car class."""
    # Task 6
    my_car = Car("330i",180)
    my_car.drive(30)
    # Task 6
    print(f"{my_car.name} has fuel: {my_car.fuel}")
    # Task 7
    print(my_car)
    # Task 1, 6
    limo = Car("Limo", 100)
    # Task 2
    limo.add_fuel(20)
    # Task 3, 6
    print(f"{limo.name} has fuel: {limo.fuel}")
    # Task 4
    limo.drive(115)
    # Task 7
    print(limo)

main()
