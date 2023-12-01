"""
CP1404/CP5632 - Practical
Password checker "skeleton" code to help you get started
"""

MIN_LENGTH = 8
MAX_LENGTH = 20
MIN_LOWERCASE = 1
MIN_UPPERCASE = 1
MIN_DIGIT = 1
MIN_SPECIAL = 1
SPECIAL_CHARS_REQUIRED = True
SPECIAL_CHARACTERS = "!@#$%^&*()_-=+`~,./'[]<>?{}|\\"


def main():
    """Program to get and check a user's password."""
    print("Please enter a valid password")
    print(f"Your password must be between {MIN_LENGTH} and {MAX_LENGTH} characters, and contain:")
    print("\t1 or more uppercase characters")
    print("\t1 or more lowercase characters")
    print("\t1 or more numbers")
    if SPECIAL_CHARS_REQUIRED:
        print(f"\tand 1 or more special characters: {SPECIAL_CHARACTERS}")
    password = input("> ")
    while not is_valid_password(password, MIN_LENGTH, MAX_LENGTH, MIN_UPPERCASE, MIN_LOWERCASE, MIN_DIGIT, MIN_SPECIAL,
                                SPECIAL_CHARS_REQUIRED, SPECIAL_CHARACTERS):
        print("Invalid password!")
        password = input("> ")
    print(f"Your {len(password)}-character password is valid: {password}")


def is_valid_password(password, min_length=8, max_length=20, min_uppercase=1, min_lowercase=1, min_digit=1,
                      min_special=1, special_chars_required=True, special_characters="!@#$%^&*()_-=+`~,./'[]<>?{}|\\"):
    """Determine if password is a valid password."""
    count_lower = 0
    count_upper = 0
    count_digit = 0
    count_special = 0
    for char in password:
        if char.isupper():
            count_upper += 1
        if char.islower():
            count_lower += 1
        if char in special_characters:
            count_special += 1
        if char.isdigit():
            count_digit += 1
    if len(password) < min_length or len(password) > max_length:
        return False
    if count_upper < min_uppercase or count_lower < min_lowercase or count_digit < min_digit:
        return False
    if special_chars_required and count_special < min_special:
        return False
    return True


main()
