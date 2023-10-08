"""CP1404 Week 05 Practicals
 Emails practice program"""


def main():
    """Create a dictionary of email addresses to names."""
    email_to_name = {}
    email = get_valid_email()
    while email != "":
        name = get_name_from_email(email)
        name_confirmation = input(f"Is your name {name}? (Y/n)").lower()
        if name_confirmation != "y" and name_confirmation != "":
            name = input("Name: ")
        email_to_name[email] = name
        print(email_to_name)
        email = get_valid_email()


def get_valid_email():
    """Get a valid email address."""
    email = input("Email: ")
    while "@" not in email:
        print("Invalid email, email must contain @")
        email = input("Email: ")
    return email


def get_name_from_email(email):
    """Get an inferred name from an email address"""
    email_name_components = email[0:email.find("@")].split(".")
    name = ' '.join(email_name_components)
    return name


main()
