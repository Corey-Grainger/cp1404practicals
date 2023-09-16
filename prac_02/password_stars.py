"""Password Stars"""

MINIMUM_PASSWORD_LENGTH = 8


def main():
    password_entered = get_password()
    print_line_of_characters(len(password_entered))


def print_line_of_characters(length):
    print("*" * length)


def get_password():
    password_entered = input("Enter password: ")
    while len(password_entered) < 8:
        print("Password must be 8 characters or more")
        password_entered = input("Enter password: ")
    return password_entered


main()
