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
            selected_filter_date = get_valid_date("Show projects that start after date (dd/mm/yyyy): ")
            filter_projects_by_date(projects, selected_filter_date)
        elif menu_choice == "A":
            print("Let's add a new project")
            add_a_project(projects)
        elif menu_choice == "U":
            update_project(projects)
        else:
            print("Invalid selection")
        print(MENU)
        menu_choice = input(">>> ").upper()
    save_projects(DEFAULT_FILENAME, projects)
    print("Thank you for using custom-built project management software")


def load_project_file(filename):
    """Load projects from filename."""
    with open(filename) as in_file:
        # Ignores first line of row headings
        projects = []
        in_file.readline()
        for line in in_file:
            parts = line.split("\t")
            parts[1] = datetime.datetime.strptime(parts[1], "%d/%m/%Y").date()
            projects.append(Project(parts[0], parts[1], int(parts[2]), float(parts[3]), int(parts[4])))
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
    for project in sorted([project for project in projects if not project.is_complete()]):
        print(f"\t{project}")
    print("Completed projects: ")
    for project in sorted([project for project in projects if project.is_complete()]):
        print(f"\t{project}")


def filter_projects_by_date(projects, date):
    """Display projects started after date"""
    for project in sorted([project for project in projects if project.start_date > date], key=attrgetter("start_date")):
        print(f"\t{project}")


def get_valid_date(prompt):
    """Get a valid date."""
    # Extract the date from a user input like 11/12/13
    date = datetime.datetime.strptime(input(prompt), "%d/%m/%Y").date()
    return date


def add_a_project(projects):
    """Add a new project to projects."""
    name = get_valid_string()
    start_date = get_valid_date("Start date (dd/mm/yyyy): ")
    priority = get_valid_number(1, 10, "Priority: ")
    cost_estimate = get_valid_cost_estimate()
    completion_percentage = get_valid_number(0, 100, "Percent complete: ")
    projects.append(Project(name, start_date, priority, cost_estimate, completion_percentage))


def get_valid_string():
    """Get a non-empty string."""
    input_string = input("Name: ")
    while input_string == "":
        print("Name cannot be blank")
        input_string = input("Name: ")
    return input_string


def get_valid_number(minimum, maximum, prompt):
    """Get a valid number between minimum and maximum inclusive."""
    number = int(input(prompt))
    return number


def get_valid_cost_estimate():
    """Get a cost estimate that isn't negative."""
    cost_estimate = float(input("Cost estimate: $"))
    return cost_estimate


def update_project(projects):
    """Update the priority and/or completion percentage of a project."""
    for i, project in enumerate(projects):
        print(f"{i} {project}")
    project_choice = get_valid_number(0, len(projects) - 1, "Project choice: ")
    new_percentage = get_valid_new_value(0, 100, "New Percentage: ", projects[project_choice].completion_percentage)
    projects[project_choice].completion_percentage = new_percentage
    new_priority = get_valid_new_value(0, 100, "New Priority: ", projects[project_choice].priority)
    projects[project_choice].priority = new_priority


def get_valid_new_value(minimum, maximum, prompt, project_value):
    """Get a valid number between minimum and maximum inclusive."""
    is_valid_value = False
    while not is_valid_value:
        number = input(prompt)
        if number != "":
            try:
                number = int(number)
                is_valid_value = True
            except ValueError:
                pass
        else:
            number = project_value
            is_valid_value = True
    return number


main()
