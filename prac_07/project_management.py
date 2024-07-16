import datetime
from prac_07.project import Project

MENU = (" - (L)oad projects\n - (S)ave projects\n - (D)isplay projects\n"
        " - (F)ilter projects by date\n - (A)dd new project\n - (U)pdate project\n - (Q)uit")
HEADING = "Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage"


def main():
    file_name = 'projects.txt'
    texts = load_file(file_name)
    for text in texts:
        print(text)
    print("Welcome to Pythonic Project Management")
    print(f'Loaded {len(texts)} projects from {file_name}')
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "L":
            file_name = input("File name: ")
            texts = load_file(file_name)
        elif choice == "S":
            file_name = input("File name: ")
            save_file(file_name, texts)
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


def save_file(file_name, texts):
    with open(file_name, 'w') as out_file:
        print(HEADING, file=out_file)
        for text in texts:
            print(text, file=out_file)


def load_file(file_name):
    texts = []
    with open(file_name, 'r') as in_file:
        in_file.readline()
        for line in in_file:
            line = line.strip().split('\t')
            texts.append(Project(line[0], line[1], line[2], line[3], line[4]))
        return texts


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
