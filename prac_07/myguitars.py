"""
CP1404 Practical
"""
from guitar import Guitar

FILENAME = "guitars.csv"


def main():
    """Extract guitars from csv file and print guitars."""
    guitars = []
    extract_guitars_from_csv(FILENAME, guitars)
    add_guitar(guitars)
    guitars.sort()
    for guitar in guitars:
        print(guitar)
    add_guitars_to_csv(FILENAME, guitars)


def extract_guitars_from_csv(filename, guitars):
    """Read from csv file and append to guitars."""
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        for line in in_file:
            parts = line.strip().split(',')
            guitar = Guitar(parts[0], int(parts[1]), float(parts[2]))
            guitars.append(guitar)


def add_guitar(guitars):
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        guitar_to_add = Guitar(name, year, cost)
        name = input("Name: ")
        guitars.append(guitar_to_add)


def add_guitars_to_csv(filename, guitars):
    with open(filename, "w", encoding="utf-8-sig") as out_file:
        for guitar in guitars:
            out_file.write(f"{guitar.name},{guitar.year},{guitar.cost}\n")


main()
