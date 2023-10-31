""""CP1404 Week 07 Practicals
My Guitars program
Estimated: 35 minutes
Started: 3:40pm
Completed: """

from guitar import Guitar
import csv

FILENAME = "guitars.csv"


def main():
    """Load and display guitar details stored in a file."""
    print(f"Welcome to My Guitars")
    guitars = load_guitars(FILENAME)
    guitars.sort()
    print(f"{len(guitars)} guitars loaded.")
    print(f"You have the following guitars:")
    for guitar in guitars:
        print(f"{guitar.name} is from {guitar.year} and costs {guitar.cost}")


def load_guitars(filename):
    """Load a list of guitars from a CSV file formatted like: Name,Year,Cost."""
    guitars = []
    with open(filename, "r") as in_file:
        reader = csv.reader(in_file)
        for row in reader:
            guitars.append(Guitar(row[0], int(row[1]), float(row[2])))
    return guitars


main()
