
"""Do This Now area for working on seminar and prac activities"""

import random

low_number = int(input("Enter low number: "))
high_number = int(input("Enter high number: "))
while high_number <= low_number:
    print("High number must be higher than low number")
    high_number = int(input("Enter high number: "))
n = random.randint(low_number,high_number)
print("=) " * n)


