"""CP1404 Week 07 Practicals
Project Management Program
Estimate: 3 hours
Commenced: 6:55pm
Break: 9:30pm
Recommenced 10:00am
Completed: 11:45am next day
Some of this time was spent researching how to use the fnmatch function."""

import datetime
from project import Project
from operator import attrgetter
from fnmatch import fnmatch

LOWEST_PRIORITY = 10
HIGHEST_PRIORITY = 1
MENU = ("(L)oad projects\n(S)ave projects\n(D)isplay projects\n"
        "(F)ilter projects by date\n(A)dd new project\n(U)pdate project\n(Q)uit")
DEFAULT_FILENAME = "projects.txt"


def main():
    """Manage and store projects for a user."""
    print(MENU)
    projects = load_project_file(DEFAULT_FILENAME)
    menu_choice = input(">>> ").upper()
    while menu_choice != "Q":
        if menu_choice == "L":
            if projects:
                continue_choice = input("Unsaved projects will be lost, continue? (y/N): ").upper()
                if continue_choice == "Y":
                    filename = get_valid_filename("Enter filename to load (e.g. filename.txt): ")
                    projects = load_project_file(filename)
                else:
                    print("File loading aborted.")
            else:
                filename = get_valid_filename("Enter filename to load (e.g. filename.txt): ")
                projects = load_project_file(filename)
        elif menu_choice == "S":
            filename = get_valid_filename("Enter name for save file (e.g. filename.txt): ")
            save_projects(filename, projects)
        elif menu_choice == "D":
            display_projects(projects)
        elif menu_choice == "F":
            selected_filter_date = get_valid_date("Show projects that start after date (dd/mm/yyyy): ")
            filter_projects_by_date(projects, selected_filter_date)
        elif menu_choice == "A":
            print("Let's add a new project")
            add_new_project(projects)
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
    projects = []
    try:
        with open(filename) as in_file:
            # Ignores first line of row headings
            in_file.readline()
            for line in in_file:
                parts = line.split("\t")
                parts[1] = datetime.datetime.strptime(parts[1], "%d/%m/%Y").date()
                # previous line makes parts[1] a valid date
                projects.append(Project(parts[0], parts[1], int(parts[2]), float(parts[3]), int(parts[4])))
    except FileNotFoundError:
        print("Filename selected for loading was not found.")
    return projects


def save_projects(filename, projects):
    """Save projects to filename."""
    with open(filename, 'w') as out_file:
        print("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage", file=out_file)
        for project in projects:
            print(f"{project.name}\t{project.start_date.__format__('%d/%m/%Y')}\t{project.priority}\t"
                  f"{project.cost_estimate}\t{project.completion_percentage}", file=out_file)
    print(f"{len(projects)} projects saves to {filename}")


def get_valid_filename(prompt):
    """Get a valid filename like filename.txt"""
    filename = input(prompt)
    while not fnmatch(filename, "*.txt"):
        print("Invalid filename.")
        filename = input(prompt)
    return filename


def display_projects(projects):
    """Displays incomplete projects and then complete projects sorted into """
    try:
        print("Incomplete projects: ")
        for project in sorted([project for project in projects if not project.is_complete()]):
            print(f"\t{project}")
        print("Completed projects: ")
        for project in sorted([project for project in projects if project.is_complete()]):
            print(f"\t{project}")
    except TypeError:
        print("No projects to display.")


def filter_projects_by_date(projects, date):
    """Display projects started after date"""
    try:
        for project in sorted([project for project in projects if project.start_date > date],
                              key=attrgetter("start_date")):
            print(f"\t{project}")
    except TypeError:
        print("No projects to display.")


def get_valid_date(prompt):
    """Get a valid date."""
    # Extract the date from a user input like 11/12/13
    is_valid_date = False
    while not is_valid_date:
        try:
            date = datetime.datetime.strptime(input(prompt), "%d/%m/%Y").date()
            if date > datetime.date.today():
                print("Start date cannot be after today")
            else:
                is_valid_date = True
        except ValueError:
            print("Invalid date.  Date must be in format dd/mm/yyyy")
    return date  # Error checking prevents variable being unassigned


def add_new_project(projects):
    """Add a new project to projects."""
    name = get_valid_name()
    start_date = get_valid_date("Start date (dd/mm/yyyy): ")
    priority = get_valid_number(HIGHEST_PRIORITY, LOWEST_PRIORITY, "Priority")
    cost_estimate = get_valid_cost_estimate(0)
    completion_percentage = get_valid_number(0, 100, "Percentage completion")
    projects.append(Project(name, start_date, priority, cost_estimate, completion_percentage))


def get_valid_name():
    """Get a non-empty string."""
    input_string = input("Name: ")
    while input_string == "":
        print("Name cannot be blank")
        input_string = input("Name: ")
    return input_string


def get_valid_number(minimum, maximum, number_name):
    """Get a valid number between minimum and maximum inclusive."""
    is_valid_input = False
    while not is_valid_input:
        try:
            number = int(input(f"{number_name}: "))
            if minimum <= number <= maximum:
                is_valid_input = True
            else:
                print(f"{number_name} must be > {minimum} and < {maximum}")
        except ValueError:
            print("Invalid input")
    return number  # Error checking prevents variable being unassigned


def get_valid_cost_estimate(minimum):
    """Get a cost estimate that isn't negative."""
    is_valid_input = False
    while not is_valid_input:
        try:
            cost_estimate = float(input("Cost estimate: $"))
            if cost_estimate > 0:
                is_valid_input = True
            else:
                print("Cost estimate must be > 0")
        except ValueError:
            print("Invalid input")
    return cost_estimate  # Error checking prevents variable being unassigned


def update_project(projects):
    """Update the priority and/or completion percentage of a project."""
    try:
        for i, project in enumerate(projects):
            print(f"{i} {project}")
        project_choice = get_valid_number(0, len(projects) - 1, "Project choice: ")
        new_percentage = get_valid_new_value(0, 100, "New Percentage", projects[project_choice].completion_percentage)
        projects[project_choice].completion_percentage = new_percentage
        new_priority = get_valid_new_value(0, 100, "New Priority", projects[project_choice].priority)
        projects[project_choice].priority = new_priority
    except TypeError:
        print("No projects to display.")


def get_valid_new_value(minimum, maximum, number_name, current_value):
    """Get a valid new value for project_value between minimum and maximum inclusive or return the previous value if
    an empty string is entered."""
    is_valid_value = False
    while not is_valid_value:
        number = input(f"{number_name}: ")
        if number != "":
            try:
                number = int(number)
                if minimum <= number <= maximum:
                    is_valid_value = True
                else:
                    print(f"{number_name} must be > {minimum} and < {maximum}. Enter nothing to keep existing value.")
            except ValueError:
                print(f"Invalid value")
        else:
            number = current_value
            is_valid_value = True
    return number  # Error checking prevents variable being unassigned


main()
