import sys
import csv

csv_files = ["before.csv"]


def main():
    try:
        output = get_csv_file(sys.argv[1], sys.argv[2])
        print(output)

    except IndexError:
        sys.exit("Too few arguments")


def get_csv_file(argument: str, argument2: str):
    if argument in csv_files:
        newCSV = []
        with open(argument) as file:
            reader = csv.DictReader(file)

            for line in reader:
                first_name, last_name = line['name'].split(",")
                house = line['house']
                newCSV.append({"first": first_name, "last": last_name, "house": house})

            with open(argument2, "w") as output:
                writer = csv.DictWriter(output, fieldnames=["first", "last", "house"])
                writer.writeheader()
                for row in newCSV:
                    writer.writerow(row)

    if len(sys.argv) < 3:
        return "Too few command-line arguments"
    elif len(sys.argv) > 3:
        return "Too many coammand-line arguments"
    elif not argument.endswith(".csv"):
        return "Not a csv file"
    elif sys.argv[1] not in csv_files:
        return f"Could not read {sys.argv[1]}"



if __name__ == "__main__":
    main()



