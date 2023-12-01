"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
    A value error will occur when the input for numerator or denominator is not a valid integer
2. When will a ZeroDivisionError occur?
    A ZeroDivisionError will occur when denominator = 0
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
    Yes.  You could add error checking to the input for denominator that doesn't allow 0.
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        print(f"Denominator cannot be 0")
        denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
print("Finished.")
