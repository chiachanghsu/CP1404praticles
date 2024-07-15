from prac_07.guitar import Guitar
import csv
FILENAME = "guitars.csv"

guitars = []
with open(FILENAME, "r") as in_file:
    reader = csv.reader(in_file)
    for record in reader:
        name = record[0]
        year = int(record[1])
        cost = float(record[2])
        guitars.append(Guitar(name, year, cost))
    guitars.sort()
    for i, guitar in enumerate(guitars, 1):
        print(i, guitar)
