"""CP1404 Week 07 Practicals
Project Management Program
Estimate: 3 hours
Commenced: 6:55pm
Break: 9:30pm
Recommenced: 10:00am next day
Break: 11:45am next day
Recommenced: 9:30pm
Complete 10:06pm
Some of this time was spent researching how to use the fnmatch function rather than actively writing the program.
Testing was the element that took a lot more time that I anticipated. """

import datetime
import csv
from operator import attrgetter
from fnmatch import fnmatch
from project import Project

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
            continue_choice = get_valid_choice("Unsaved projects will be lost. Continue? (y/n): ")
            if continue_choice == "Y":
                filename = get_valid_filename("Enter filename to load (e.g. filename.txt): ")
                projects = load_project_file(filename)
            else:
                print("File loading cancelled.")
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
    # Error checking of save_choice helps prevent accidental loss of data
    save_choice = get_valid_choice(
        f"Saving will overwrite existing save data in {DEFAULT_FILENAME}.  Save projects? (y/n)? ")
    if save_choice == "Y":
        save_projects(DEFAULT_FILENAME, projects)
    print("Thank you for using custom-built project management software")


def get_valid_choice(prompt):
    """Get a valid choice, either Y or N."""
    save_choice = input(prompt).upper()
    while save_choice != "Y" and save_choice != "N":
        save_choice = input(prompt).upper()
    return save_choice


def load_project_file(filename):
    """Load projects from filename."""
    projects = []
    try:
        with open(filename, encoding="UTF-8") as in_file:
            # Ignores first line of row headings
            in_file.readline()
            for line in in_file:
                parts = line.split("\t")
                parts[1] = datetime.datetime.strptime(parts[1], "%d/%m/%Y").date()
                # preceding line makes parts[1] a valid date
                projects.append(Project(parts[0], parts[1], int(parts[2]), float(parts[3]), int(parts[4])))
    except FileNotFoundError:
        print("Filename selected for loading was not found.")
    return projects


def save_projects(filename, projects):
    """Save projects to filename."""
    with open(filename, 'w', encoding="UTF-8") as out_file:
        writer = csv.writer(out_file, delimiter="\t")
        # add the appropriate headers to the file
        writer.writerow(["Name", "Start Date", "Priority", "Cost Estimate", "Completion Percentage"])
        for project in projects:
            writer.writerow(
                [project.name, project.start_date.strftime('%d/%m/%Y'), project.priority, project.cost_estimate,
                 project.completion_percentage])


def get_valid_filename(prompt):
    """Get a valid filename like filename.txt"""
    filename = input(prompt)
    # check that filename matches format like filename.txt
    while not fnmatch(filename, "*.txt"):
        print("Invalid filename.")
        filename = input(prompt)
    return filename


def display_projects(projects):
    """Displays incomplete projects and then complete projects sorted into """
    try:
        print("Incomplete projects: ")
        # print each project in projects sorted by priority if the project is incomplete
        for project in sorted([project for project in projects if not project.is_complete()]):
            print(f"\t{project}")
        print("Completed projects: ")
        # print each project in projects sorted by priority if the project is complete
        for project in sorted([project for project in projects if project.is_complete()]):
            print(f"\t{project}")
    except TypeError:
        print("No projects to display.")


def filter_projects_by_date(projects, selected_filter_date):
    """Display projects started after date"""
    try:
        # print each project in projects sorted by the date if the project start date is after date
        for project in sorted([project for project in projects if project.start_date > selected_filter_date],
                              key=attrgetter("start_date")):
            print(f"\t{project}")
    except TypeError:
        print("No projects to display.")


def get_valid_date(prompt):
    """Get a valid date that is after the current date."""
    # Extract the date from a user input like 11/12/13
    is_valid_date = False
    while not is_valid_date:
        try:
            date = datetime.datetime.strptime(input(prompt), "%d/%m/%Y").date()
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
            print("Invalid input.")
    return number  # Error checking prevents variable being unassigned


def get_valid_cost_estimate(minimum):
    """Get a cost estimate that isn't negative."""
    is_valid_input = False
    while not is_valid_input:
        try:
            cost_estimate = float(input("Cost estimate: $"))
            if cost_estimate >= minimum:
                is_valid_input = True
            else:
                print(f"Cost estimate cannot be less than {minimum}.")
        except ValueError:
            print("Invalid input.")
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
    """Get a valid value between minimum and maximum inclusive or return the current value if
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
                print("Invalid value. Must be a whole number.")
        else:
            number = current_value
            is_valid_value = True
    return number  # Error checking prevents variable being unassigned


main()
