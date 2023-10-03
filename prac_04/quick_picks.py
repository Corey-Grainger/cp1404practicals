"""CP1404 Week 4 Prac Quick pick Lottery Ticket Generator"""

import random

MINIMUM = 1
MAXIMUM = 45
NUMBER_OF_NUMBERS = 6


def main():
    """Quick pick lottery ticket generator."""
    number_of_quick_picks = get_valid_number()
    for i in range(number_of_quick_picks):
        numbers = []
        generate_quick_pick(numbers, NUMBER_OF_NUMBERS, MINIMUM, MAXIMUM)
        print_quick_pick(numbers)


def generate_quick_pick(numbers, number_of_numbers, minimum, maximum):
    """Generate number_of_numbers random integers between minimum and maximum."""
    for i in range(number_of_numbers):
        number = random.randint(minimum, maximum)
        while number in numbers:
            number = random.randint(minimum, maximum)
        numbers.append(number)


def get_valid_number():
    """Get a valid integer."""
    is_valid_number = False
    while not is_valid_number:
        try:
            number = int(input("How many quick picks? "))
            is_valid_number = True
        except ValueError:
            print("Number must be a valid integer")
    return number  # Loop prevents unassigned value


def print_quick_pick(numbers):
    """Print numbers formatted into columns."""
    numbers.sort()
    for number in numbers:
        print(f"{number:2}", end=" ")
    print()


main()
