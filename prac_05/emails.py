"""CP1404 Week 05 Practicals
 Emails practice program"""

email_to_name = {}
email = input("Email: ")
while email != "":
    while "@" not in email:
        print("Invalid email, email must contain @ character")
        email = input("Email: ")
    email_name_components = email[0:email.find("@")].split(".")
    print(email_name_components)
