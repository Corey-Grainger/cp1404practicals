""""CP1404 Week 07 Practicals
My Guitars program
Estimated: 35 minutes
Started: 3:40pm
Completed: 4:08pm"""

import csv
from guitar import Guitar

FILENAME = "guitars.csv"
MENU = "(A)dd guitars\n(D)isplay Guitars\nSave an (Q)uit"


def main():
    """Load and display guitar details stored in a file."""
    print("Welcome to My Guitars")
    guitars = load_guitars(FILENAME)
    guitars.sort()
    print(f"{len(guitars)} guitars loaded.")
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "D":
            display_guitars(guitars)
        elif choice == "A":
            add_new_guitars(guitars)
        else:
            print("Invalid selection.")
        print(MENU)
        choice = input(">>> ").upper()
    save_guitars(FILENAME, guitars)


def display_guitars(guitars):
    """Display each guitar in guitars."""
    print("You have the following guitars:")
    for guitar in guitars:
        print(f"{guitar.name:30} is from {guitar.year:4} and costs {guitar.cost:.2f}")


def add_new_guitars(guitars):
    """Get new guitars until the user enters an empty string."""
    print("Enter details of new guitars.  Enter a blank name to stop.")
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: "))
        guitars.append(Guitar(name, year, cost))
        print(f"{name} ({year}) : ${cost:.2f} added.")
        name = input("Name: ")


def load_guitars(filename):
    """Load a list of guitars from a CSV file formatted like: Name,Year,Cost."""
    guitars = []
    with open(filename, "r", encoding="UTF-8") as in_file:
        reader = csv.reader(in_file)
        for row in reader:
            guitars.append(Guitar(row[0], int(row[1]), float(row[2])))
    return guitars


def save_guitars(filename, guitars):
    """Save guitars to filename as a CSV file with each line formatted like: Name,Year,Cost."""
    with open(filename, "w", newline='', encoding="UTF-8") as out_file:  # use default dialect
        writer = csv.writer(out_file)
        for guitar in guitars:
            writer.writerow([guitar.name, guitar.year, guitar.cost])


main()
