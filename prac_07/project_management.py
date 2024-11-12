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
            pass
        elif choice == "U":
            pass
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


main()
