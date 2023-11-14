"""CP1404 Week 09 Practicals
Taxi Simulator
Estimated: 45 minutes
Started 3:48pm"""

from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi

MENU = f"q)uit, c)hoose taxi, d)rive"




def main():
    print("Let's drive!")
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    current_taxi = None
    bill = 0.0
    print(MENU)
    choice = input(">>> ").lower()
    while choice != "q":
        if choice == "c":
            display_taxis(taxis)
            taxi_choice = get_valid_choice(taxis)
            current_taxi = taxis[taxi_choice]
        elif choice == "d":
            if current_taxi:
                requested_distance = get_valid_number()
                current_taxi.drive(distance=requested_distance)
            else:
                print("You need to choose a taxi before you can drive")
        else:
            print("Invalid option")
        bill += current_taxi.get_fare()
        print(f"Bill to date: ${bill:.2f}")


def display_taxis(taxis):
    pass


def get_valid_choice(taxis):
    pass


def get_valid_number():
    pass


main()
