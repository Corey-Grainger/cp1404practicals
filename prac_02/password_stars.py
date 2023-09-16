"""Password Stars"""

minimum_password_length = 8
password_entered = input("Enter password: ")
while len(password_entered) < 8:
    print("Password must be 8 characters or more")
    password_entered = input("Enter password: ")
print("*" * len(password_entered))
