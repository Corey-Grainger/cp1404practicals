"""CP1404 Week 05 Practicals
 Emails practice program"""


def main():
    email_to_name = {}
    email = get_valid_email()
    while email != "":
        email_name_components = email[0:email.find("@")].split(".")
        name = ' '.join(email_name_components)
        name_confirmation = input(f"Is your name {name}? (Y/n)").lower()
        if name_confirmation != "y" and name_confirmation != "":
            name = input("Name: ")
        email_to_name[email] = name
        print(email_to_name)
        email = get_valid_email()


def get_valid_email():
    email = input("Email: ")
    while "@" not in email:
        print("Invalid email, email must contain @ character")
        email = input("Email: ")
    return email


main()