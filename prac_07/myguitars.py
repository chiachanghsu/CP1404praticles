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
is_finished = False
while not is_finished:
    try:
        name = input("Name: ")
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        is_finished = True
    except ValueError:
        print("Invalid input")
guitars.append(Guitar(name, year, cost))
guitars.sort()
for i, guitar in enumerate(guitars, 1):
    print(i, guitar)
with open(FILENAME, "w") as out_file:
    writer = csv.writer(out_file)
    for guitar in guitars:
        print(f"{guitar.name},{guitar.year},{guitar.cost}", file=out_file)
