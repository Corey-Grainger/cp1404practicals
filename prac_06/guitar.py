"""CP1404 Week 06 Practicals
Guitar Class
Estimate: 15 minutes
Started: 2:50pm
Completed: 3:06pm"""


class Guitar:
    def __init__(self, name="", year=1590, cost=0.0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return f"{self.name} ({self.year}) : ${self.cost:.2f})"

    def get_age(self):
        return 2023 - self.year

    def is_vintage(self):
        return (self.get_age()) >= 50


if __name__ == '__main__':
    guitar = Guitar("Gibson l-5 CES", 1922, 16035.40)
    print(guitar)
    print(guitar.name)
    print(guitar.year)
    print(guitar.cost)
    print(guitar.get_age())
    print(guitar.is_vintage())

