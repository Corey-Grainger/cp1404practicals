"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    data = get_data()
    for datum in data:
        print(f"{datum[0]} is taught by {datum[1]:12} and has {datum[2]:3} students")


def get_data():
    """Return subject data as a list from a file formatted like: subject,lecturer,number of students."""
    data = []
    input_file = open(FILENAME)
    for line in input_file:
        line = line.strip()
        parts = line.split(',')
        parts[2] = int(parts[2])  # Will be valid int in correctly formatted file
        data.append(parts)
    input_file.close()
    return data


main()
