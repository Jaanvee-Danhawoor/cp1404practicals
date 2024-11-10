"""
Guitar program.
Estimate: 20 minutes
Actual:   25 minutes
"""
from prac_06.guitar import Guitar


def main():
    """Guitar program, using Guitar class."""
    guitars = []
    print("My guitars!")
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        guitar_to_add = Guitar(name, year, cost)
        name = input("Name: ")
        guitars.append(guitar_to_add)
    display_guitars(guitars)


def display_guitars(guitars):
    if guitars:
        print("These are my guitars:")
        for i, guitar in enumerate(guitars, 1):
            vintage_string = ""
            if guitar.is_vintage():
                vintage_string = " (vintage)"
            print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_string}")


main()
