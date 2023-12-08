FILENAME = "wimbledon.csv"
INDEX_COUNTRY = 1
INDEX_CHAMPION = 2


def main():
    records = get_records(FILENAME)
    champion_to_count, countries = process_records(records)
    display_results(champion_to_count, countries)


def process_records(records):
    count_record = {}
    countries = set()
    for record in records:
        countries.add(record[INDEX_COUNTRY])
        try:
            count_record[record[INDEX_CHAMPION]] += 1
        except KeyError:
            count_record[record[INDEX_CHAMPION]] = 1
    return count_record, countries


def display_results(count_record, countries):
    print("Wimbledon Champions: ")
    for name, count in count_record.items():
        print(name, count)
    print(f"\nThese {len(countries)} countries have won Wimbledon: ")
    print(", ".join(country for country in sorted(countries)))


def get_records(filename):
    records = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()
        for line in in_file:
            parts = line.strip().split(",")
            records.append(parts)
    return records


main()