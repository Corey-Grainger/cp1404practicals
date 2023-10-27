"""CP1404 Week 06 Practicals
Guitar class testing program
Estimated: 10 minutes
Commenced: 3:06pm
Completed: 3:12pm"""

from guitar import Guitar

gibson = Guitar("Gibson l-5 CES", 1922, 16035.40)
another_guitar = Guitar("Another Guitar", 2013)
default_guitar = Guitar()

print(f"{gibson.name} get_age() - Expected 101. Got {gibson.get_age()}")
print(f"{another_guitar.name} get_age() - Expected 10. Got {another_guitar.get_age()}")
print(f"{another_guitar.name} get_age() - Expected 433. Got {another_guitar.get_age()}")
print(f"{gibson.name} is_vintage() - Expected True. Got {gibson.is_vintage()}")
print(f"{another_guitar.name} is_vintage() - Expected False. Got {another_guitar.is_vintage()}")
print(f"{another_guitar.name} is_vintage() - Expected True. Got {another_guitar.is_vintage()}")

