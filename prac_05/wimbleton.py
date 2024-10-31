"""
Wimbledon
Estimate: 20 minutes
Actual:   25 minutes

"""
FILENAME = "wimbledon.csv"
INDEX_COUNTRY = 1
INDEX_CHAMPION = 2


def main():
    """Read csv file, process data and print details about Wimbledon champions and countries."""
    records = get_records(FILENAME)
    champion_to_count, countries = process_records(records)
    display_results(champion_to_count, countries)


def get_records(filename):
    """Get records from csv file in list of lists form."""
    records = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()
        for line in in_file:
            parts = line.strip().split(",")
            records.append(parts)
    return records


def process_records(records):
    """Create dictionary of champion_to_count and set of countries from records."""
    champion_to_count = {}
    countries = set()
    for record in records:
        countries.add(record[INDEX_COUNTRY])
        champion_to_count[record[INDEX_CHAMPION]] = champion_to_count.get(record[INDEX_CHAMPION], 0) + 1
    return champion_to_count, countries


def display_results(champion_to_count, countries):
    """Display champions and countries."""
    print("Wimbledon Champions: ")
    for champion_name, count in champion_to_count.items():
        print(champion_name, count)
    print(f"\nThese {len(countries)} countries have won Wimbledon: ")
    print(", ".join(country for country in sorted(countries)))


main()
