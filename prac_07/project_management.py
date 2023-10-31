"""CP1404 Week 07 Practicals
Project Management Program
Estimate: 3 hours
Commenced: 6:55pm
Completed: """

import datetime
from project import Project
from operator import attrgetter

MENU = ("(L)oad projects\n(S)ave projects\n(D)isplay projects\n"
        "(F)ilter projects by date\n(A)dd new project\n(U)pdate project\n(Q)uit")
DEFAULT_FILENAME = "projects.txt"


def main():
    """Manage and store projects for a user"""
    print(MENU)
    projects = load_project_file(DEFAULT_FILENAME)
    menu_choice = input(">>> ").upper()
    while menu_choice != "Q":
        if menu_choice == "L":
            if projects:
                continue_choice = input("Unsaved projects will be lost, continue? (y/N): ").upper()
                if continue_choice == "Y":
                    filename = get_valid_filename()
                    load_project_file(filename)
                else:
                    print("File loading aborted.")
        elif menu_choice == "S":
            filename = get_valid_filename()
            save_projects(filename, projects)
        elif menu_choice == "D":
            display_projects(projects)
        elif menu_choice == "F":
            selected_filter_date = get_valid_date()
            filter_projects_by_date(projects, selected_filter_date)
        elif menu_choice == "A":
            print("Add new project")
        else:
            print("Invalid selection")
        print(MENU)
        menu_choice = input(">>> ").upper()
    save_projects(DEFAULT_FILENAME, projects)
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
    projects.sort()
    return projects


def save_projects(filename, projects):
    """Save projects to filename."""
    with open(filename, 'w') as out_file:
        print("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage", file=out_file)
        for project in projects:
            print(f"{project.name}\t{project.start_date.__format__('%d/%m/%Y')}\t{project.priority}\t"
                  f"{project.cost_estimate}\t{project.completion_percentage}", file=out_file)
    print(f"{len(projects)} projects saves to {filename}")


def get_valid_filename():
    """Get a valid filename like filename.txt"""
    filename = input("Enter filename to load (e.g. filename.txt): ")
    return filename


def display_projects(projects):
    """Displays projects """
    print("Incomplete projects: ")
    for project in [project for project in projects if not project.is_complete()]:
        print(f"\t{project}")
    print("Completed projects: ")
    for project in [project for project in projects if project.is_complete()]:
        print(f"\t{project}")


def filter_projects_by_date(projects, date):
    """Display projects started after date"""
    date_filtered_projects = [project for project in projects if project.start_date > date]
    date_filtered_projects.sort(key=attrgetter("start_date"))
    for project in date_filtered_projects:
        print(f"\t{project}")


def get_valid_date():
    """Get a valid date."""
    # Extract the date from a user input like 11/12/13
    date = datetime.datetime.strptime(input("Show projects that start after date (dd/mm/yyyy): "), "%d/%m/%Y").date()
    return date


main()
