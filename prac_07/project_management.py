"""
Project Management Program
Estimate: 3 hours
Actual:
"""
from datetime import datetime
from project import Project

DEFAULT_FILENAME = "projects.txt"
MENU = ("(L)oad projects\n(S)ave projects\n(D)isplay projects\n"
        "(F)ilter by date\n(A)dd new project\n(U)pdate project")


def main():
    projects = []
    load_projects(projects, DEFAULT_FILENAME)
    print(MENU)
    choice = input("Enter your choice: ").upper()
    while choice != "Q":
        if choice == "L":
            filename = input("Enter filename: ")
            load_projects(projects, filename)
        elif choice == "S":
            pass
        elif choice == "D":
            display_incomplete_projects(projects)
            display_completed_projects(projects)
        elif choice == "F":
            date = get_valid_date("Show projects that start after date (dd/mm/yy): ")
            filtered_projects_by_date = filter_projects_by_date(date, projects)
            display_incomplete_projects(filtered_projects_by_date)
        elif choice == "A":
            add_new_project(projects)
        elif choice == "U":
            update_project(projects)
        else:
            print("Invalid choice.")
        print(MENU)
        choice = input("Enter your choice: ").upper()


def load_projects(projects, filename):
    """Load projects from file."""
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()  # Ignore header
        for line in in_file:
            parts = line.strip().split("\t")
            start_date = datetime.strptime(parts[1], "%d/%m/%Y").date()
            project = Project(parts[0], start_date, int(parts[2]), float(parts[3]), float(parts[4]))
            projects.append(project)


def display_incomplete_projects(projects):
    """Display incomplete projects."""
    projects.sort()
    print("Incomplete Projects:")
    [print(project) for project in projects if not project.is_complete()]


def display_completed_projects(projects):
    """Display completed projects."""
    projects.sort()
    print("Completed Projects:")
    [print(project) for project in projects if project.is_complete()]


def get_valid_date(prompt):
    """Get a valid date."""
    is_valid_date = False
    while not is_valid_date:
        date_string = input(prompt).strip()
        try:
            valid_date = datetime.strptime(date_string, "%d/%m/%Y").date()
            is_valid_date = True
        except ValueError:
            print("Invalid date format. Please use dd/mm/yyyy.")
    return valid_date  # There will not be a case where this is unassigned.


def filter_projects_by_date(date, projects):
    """Filter projects by date."""
    filtered_projects_by_date = [project for project in projects if project.start_date > date]
    return filtered_projects_by_date


def get_valid_name(prompt):
    """Get a valid name that is not empty."""
    valid_name = input(prompt).strip()
    while not valid_name:
        print("Input cannot be empty")
        valid_name = input(prompt).strip()
    return valid_name


def get_valid_number(prompt):
    """Get a valid number."""
    is_valid_number = False
    while not is_valid_number:
        try:
            valid_number = float(input(prompt))
            if valid_number <= 0:
                print("Number must be > 0")
            else:
                is_valid_number = True
        except ValueError:
            print("Invalid input; enter a valid number")
    return valid_number  # There will not be a case where this is unassigned.


def get_valid_percentage(prompt):
    """Get a valid percentage between 0 and 100"""
    is_valid_input = False
    while not is_valid_input:
        try:
            percentage = float(input(prompt))
            if 0 <= percentage <= 100:
                is_valid_input = True
            else:
                print("Completion percentage must be between 0 and 100.")
        except ValueError:
            print("Invalid percentage; enter a valid number")
    return percentage  # There will not be a case where this is unassigned.


def add_new_project(projects):
    print("Let's add a new project")
    name = get_valid_name("Name: ").title()
    start_date = get_valid_date("Start date (dd/mm/yyyy): ")
    priority = int(get_valid_number("Priority: "))
    cost_estimate = get_valid_number("Cost estimate: ")
    completion_percentage = get_valid_percentage("Percent complete: ")
    new_project = Project(name, start_date, priority, cost_estimate, completion_percentage)
    projects.append(new_project)


def display_all_projects_with_index(projects):
    for i, project in enumerate(projects):
        print(f"{i} {project}")


def get_valid_project(projects, prompt):
    """Get a valid index below the length of the list."""
    is_valid_index = False
    while not is_valid_index:
        try:
            valid_index = int(input(prompt))
            valid_project = projects[valid_index]
        except KeyError:
            print(f"Invalid index; index must be between 0 and {len(projects) - 1} inclusive")
        except ValueError:
            print("Invalid input; enter a valid number")
    return valid_project  # There will not be a case where this is unassigned.


def update_project(projects):
    selected_project = get_valid_project(projects, "Project Choice: ")
    print(selected_project)
    new_percentage = get_valid_percentage("New percentage: ")
    new_priority = get_valid_number("New priority: ")
    selected_project.completion_percentage = new_percentage
    selected_project.priority = new_priority


main()
