"""CP1404 Week 06 Practicals
Guitar Class
Estimate: 15 minutes
Commenced: 2:50pm
Completed: 3:06pm"""

import datetime


class Guitar:
    """Represent a guitar object."""
    VINTAGE_THRESHOLD = 50

    def __init__(self, name="", year=1590, cost=0.0):
        """Initialise a guitar instance."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return the string version of a guitar."""
        return f"{self.name} ({self.year}) : ${self.cost:.2f})"

    def __repr__(self):
        """Return a string representation of a guitar."""
        return f"{self.name} ({self.year}) : ${self.cost:.2f})"

    def get_age(self):
        """Gets the age of guitar by subtracting its year of manufacture from current year."""
        return datetime.date.today().year - self.year

    def is_vintage(self):
        """Determine if guitar is vintage."""
        return self.get_age() >= self.VINTAGE_THRESHOLD

    def __lt__(self, other):
        """Determine if one Guitar is < another based on their year's"""
        return self.year < other.year


if __name__ == '__main__':
    guitar = Guitar("Gibson l-5 CES", 1922, 16035.40)
    print(guitar)
    print(guitar.name)
    print(guitar.year)
    print(guitar.cost)
    print(guitar.get_age())
    print(guitar.is_vintage())
