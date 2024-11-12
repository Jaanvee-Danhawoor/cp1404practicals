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
            display_projects(projects)
        elif choice == "F":
            pass
        elif choice == "A":
            pass
        elif choice == "U":
            pass
        else:
            print("Invalid choice")
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


def display_projects(projects):
    """Display projects."""
    projects.sort()
    print("Completed Projects:")
    [print(project) for project in projects if project.is_complete()]
    print("Incomplete Projects:")
    [print(project) for project in projects if not project.is_complete()]


main()
