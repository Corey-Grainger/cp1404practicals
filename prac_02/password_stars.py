"""Password Stars"""

MINIMUM_PASSWORD_LENGTH = 8


def main():
    password_entered = get_password(MINIMUM_PASSWORD_LENGTH)
    print_line_of_characters(len(password_entered))


def print_line_of_characters(length):
    print("*" * length)


def get_password(minimum_password_length):
    """Get a password with a minimum length"""
    password_entered = input("Enter password: ")
    while len(password_entered) < minimum_password_length:
        print("Password must be 8 characters or more")
        password_entered = input("Enter password: ")
    return password_entered


main()
