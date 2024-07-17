from prac_06.guitar import Guitar

guitars = [Guitar("Gibson L-5 CES", 1922, 16035.40),
           Guitar("Line 6 JTV-59", 2010, 1512.9)]
name = input("Name: ").title()
is_finished = False
while not is_finished:
    try:
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        is_finished = True
    except ValueError:
        print("Invalid input")
guitars.append(Guitar(name, year, cost))

for i, guitar in enumerate(guitars, 1):
    # do something with i (the index) and guitar (the element)
    if Guitar.is_vintage(guitar):
        vintage_string = "(vintage)"
    else:
        vintage_string = ""
    print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f} {vintage_string}")
