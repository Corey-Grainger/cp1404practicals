"""CP1404 Week 09 Practicals
Taxi Simulator
Estimated: 45 minutes
Commenced: 3:48pm
Break: 4:06pm - 6:50pm
Completed: 7:04pm"""

from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi

MENU = f"q)uit, c)hoose taxi, d)rive"


def main():
    """Taxi simulator program."""
    print("Let's drive!")
    taxis = [Taxi("Prius", 100), SilverServiceTaxi(2, fuel=100, name="Limo"),
             SilverServiceTaxi(4, fuel=200, name="Hummer")]
    current_taxi = None
    bill = 0
    print(MENU)
    choice = input(">>> ").lower()
    while choice != "q":
        if choice == "c":
            display_taxis(taxis)
            current_taxi = choose_valid_taxi(taxis)
        elif choice == "d":
            if current_taxi:
                fare = simulate_taxi_trip(current_taxi)
                print(f"Your {current_taxi.name} trip cost you ${fare:.2f}")
                bill += fare
            else:
                print("You need to choose a taxi before you can drive")
        else:
            print("Invalid option")

        print(f"Bill to date: ${bill:.2f}")
        choice = input(">>> ").lower()
    print(f"Total trip cost: ${bill:.2f}")
    print(f"Taxis are now: ")
    display_taxis(taxis)


def simulate_taxi_trip(current_taxi):
    """Simulate a taxi trip."""
    requested_distance = get_valid_number()
    current_taxi.start_fare()
    current_taxi.drive(requested_distance)
    fare = current_taxi.get_fare()
    return fare


def display_taxis(taxis):
    """Display each taxi and its index."""
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")


def choose_valid_taxi(taxis):
    """Get a valid index for a taxi."""
    try:
        choice = int(input("Choose taxi: "))
        if choice < 0 or choice > len(taxis) - 1:
            print("Invalid taxi choice")
            return None
        return taxis[choice]
    except ValueError:
        print("Invalid taxi choice")
        return None


def get_valid_number():
    """Get a valid number that is >= 0."""
    is_valid_number = False
    while not is_valid_number:
        try:
            number = float(input("Drive how far? "))
            if number >= 0:
                is_valid_number = True
                return number
            print("Distance cannot be negative")
        except ValueError:
            print("Distance must be a valid number")


main()
