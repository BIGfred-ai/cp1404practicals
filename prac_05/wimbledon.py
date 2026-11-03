
"""Display Wimbledon champions and their countries.
Estimate: 40 minutes
Actual:  60 minutes
"""

import csv

FILENAME = "wimbledon.csv"
COUNTRY_INDEX = 1
CHAMPION_INDEX = 2


def main():
    """Read Wimbledon data and display the results."""
    records = read_data(FILENAME)
    champion_to_count, countries = process_data(records)
    display_results(champion_to_count, countries)


def read_data(filename):
    """Read the CSV file into a list of lists."""
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        reader = csv.reader(in_file)
        next(reader)  # Skip the header
        records = list(reader)
    return records


def process_data(records):
    """Count champion wins and collect unique countries."""
    champion_to_count = {}
    countries = set()

    for record in records:
        champion = record[CHAMPION_INDEX]
        country = record[COUNTRY_INDEX]

        if champion in champion_to_count:
            champion_to_count[champion] += 1
        else:
            champion_to_count[champion] = 1

        countries.add(country)

    return champion_to_count, countries


def display_results(champion_to_count, countries):
    """Display champion counts and sorted countries."""
    print("Wimbledon Champions!:")

    for champion, count in champion_to_count.items():
        print(f"{champion} {count}")

    print()
    print(f"These {len(countries)} countries have won Wimbledon:")
    print(", ".join(sorted(countries)))


if __name__ == "__main__":
    main()
