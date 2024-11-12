"""
CP1404 Practical
"""
from guitar import Guitar

FILENAME = "guitars.csv"


def main():
    """Extract guitars from csv file and print guitars."""
    guitars = []
    extract_guitars_from_csv(FILENAME, guitars)
    guitars.sort()
    for guitar in guitars:
        print(guitar)


def extract_guitars_from_csv(filename, guitars):
    """Read from csv file and append to guitars."""
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        for line in in_file:
            parts = line.strip().split(',')
            guitar = Guitar(parts[0], int(parts[1]), float(parts[2]))
            guitars.append(guitar)


main()
