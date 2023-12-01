
"""More temperatures program"""


def main():
    """Read a file of Fahrenheit temperatures, convert them to Celsius and save them to a file"""
    in_file = open("temps_input.txt")
    out_file = open("temps_output.txt", "w")
    for line in in_file:
        fahrenheit = float(line)
        celsius = convert_fahrenheit_to_celsius(fahrenheit)
        print(celsius, file=out_file)
    in_file.close()
    out_file.close()


def convert_fahrenheit_to_celsius(fahrenheit):
    """Convert temperature in Fahrenheit to Celsius."""
    celsius = 5 / 9 * (fahrenheit - 32)
    return celsius


main()
