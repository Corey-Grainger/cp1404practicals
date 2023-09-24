
"""CP1404/CP5632 - Practical 3 files.py"""

with open("name.txt", "w") as out_file:
    name = input("Enter your name: ")
    print(name, file=out_file)

with open("name.txt", "r") as in_file:
    print(f"Your name is {in_file.read().strip()}")

with open("numbers.txt") as in_file:
    print(f"{int(in_file.readline()) + int(in_file.readline())}")

with open("numbers.txt") as in_file:
    total = 0
    for line in in_file:
        total += int(line)
    print(total)
