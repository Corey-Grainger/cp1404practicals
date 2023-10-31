"""CP1404 Week 07 Practicals
Project Management Program"""

import datetime
from project import Project
from operator import attrgetter

MENU = "(L)oad projects\n(S)ave projects\n(D)isplay projects\n(F)ilter projects by date\n(A)dd new project\n(U)pdate project\n(Q)uit"
DEFAULT_FILENAME = "projects.txt"


def main():
    """Manage and store projects for a user"""
    print(MENU)
    projects = load_project_file(DEFAULT_FILENAME)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "L":
            print("Load")
        elif choice == "S":
            print("Save")
        elif choice == "D":
            display_projects(projects)
        elif choice == "F":
            print("filter projects")
        elif choice == "A":
            print("Add new project")
        else:
            print("Invalid selection")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you for using custom-built project management software")


def load_project_file(filename):
    """Load projects from filename sorted by date."""
    with open(filename) as in_file:
        # Ignores first line of row headings
        projects = []
        in_file.readline()
        for line in in_file:
            parts = line.split("\t")
            parts[1] = datetime.datetime.strptime(parts[1], "%d/%m/%Y").date()
            projects.append(Project(parts[0], parts[1], int(parts[2]), float(parts[3]), int(parts[4])))
    projects.sort(key=attrgetter("start_date"))
    return projects


def display_projects(projects):
    for project in projects:
        print(project)


main()
