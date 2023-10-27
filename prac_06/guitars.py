"""CP1404 Week 06 Practicals
Guitars program
Estimated: 25 minutes
Commenced: 3:21pm
Completed: 3:38pm"""

from guitar import Guitar

print("My Guitars")
guitars = []
name = input("Name: ")
while name != "":
    year = int(input("Year: "))
    cost = float(input("Cost: "))
    guitars.append(Guitar(name, year, cost))
    print(f"{name} ({year}) : ${cost:.2f} added.")
    name = input("Name: ")
if not guitars:
    print("You have no guitars.")
else:
    print("These are my guitars:")
    for i, guitar in enumerate(guitars, 1):
        vintage_string = " (vintage)" if guitar.is_vintage() else ""
        print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:>10,.2f}{vintage_string}")
