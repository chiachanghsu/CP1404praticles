import datetime


FILE_NAME = 'projects.txt'
MENU = (" - (L)oad projects\n - (S)ave projects\n - (D)isplay projects\n"
        " - (F)ilter projects by date\n - (A)dd new project\n - (U)pdate project\n - (Q)uit")


def main():
    text = []
    with open(FILE_NAME, 'r') as in_file:
        in_file.readline()
        for line in in_file:
            text.append(line)
    print("Welcome to Pythonic Project Management")
    print(f'Loaded {len(text)} projects from {FILE_NAME}')
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "L":
            pass
        elif choice == "S":
            pass
        elif choice == "D":
            pass
        elif choice == "F":
            pass
        elif choice == "A":
            pass
        elif choice == "U":
            pass
        else:
            print("Invalid input.")
        choice = input(">>> ").upper()
    print("Thank you for using custom-built project management software.")
    # print(text)



# for line in in_file:
#     index_of_slash = line.find('/')
#     starting_of_date = index_of_slash - 2
#     ending_of_date = index_of_slash + 8
#     # print(line[starting_of_date:ending_of_date])
#     date_string = line[starting_of_date:ending_of_date]
#     date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
#     print(f"That day is/was {date.strftime('%A')}")
#     print(date.strftime("%d/%m/%Y"))
main()
