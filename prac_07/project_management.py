"""CP1404 Week 07 Practicals
Project Management Program"""

from project import Project

MENU = "(L)oad projects\n(S)ave projects\n(D)isplay projects\n(F)ilter projects by date\n(A)dd new project\n(U)pdate project\n(Q)uit"

def main():
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "L":
            print("Load")
        elif choice == "S":
            print("Save")
        elif choice == "D":
            print("Display projects")
        elif choice == "F":
            print("filter projects")
        elif choice == "A":
            print("Add new project")
        else:
            print("Invalid selection")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you for using custom-built project management software")

main()
