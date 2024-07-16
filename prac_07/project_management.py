import datetime
from prac_07.project import Project

MENU = (" - (L)oad projects\n - (S)ave projects\n - (D)isplay projects\n"
        " - (F)ilter projects by date\n - (A)dd new project\n - (U)pdate project\n - (Q)uit")
HEADING = "Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage"
YES_NO = ["Y", "YES", "N", "NO"]


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
        if choice == "L" or choice == "S":
            file_name = input("File name: ")
            try:
                if choice == 'L':
                    texts = load_file(file_name)
                elif choice == 'S':
                    save_file(file_name, texts)
            except FileNotFoundError:
                print("No file found.")
        elif choice == "D":
            display_file(texts)
        elif choice == "F":
            pass
        elif choice == "A":
            print("Let's add a new project.")
            name = input("Name: ").title()
            date = input("Start date (dd/mm/yy): ")
            priority = input("Priority: ")
            cost = input("Cost estimate: $")
            percentage = input("Percentage: ")
            texts.append(Project(name, date, priority, cost, percentage))
        elif choice == "U":
            pass
        else:
            print("Invalid input.")
        print(MENU)
        choice = input(">>> ").upper()
    save_choice = input(f"Would you like to save to {file_name}?(Y/N) ").upper()
    while save_choice not in YES_NO:
        print("Invalid input.")
        save_choice = input(f"Would you like to save to {file_name}?(Y/N) ").upper()
    if save_choice == "Y" or save_choice == "YES":
        save_file(file_name, texts)
        print("Saved.")
    print("Thank you for using custom-built project management software.")


def display_file(texts):
    incomplete_projects = []
    complete_projects = []
    for text in texts:
        if int(text.percentage) < 100:
            incomplete_projects.append(Project(text.name, text.date, text.priority, text.cost, text.percentage))
        else:
            complete_projects.append(Project(text.name, text.date, text.priority, text.cost, text.percentage))
    print("Incomplete projects:")
    incomplete_projects.sort(), complete_projects.sort()
    for project in incomplete_projects:
        print(f"\t{project.name}, start: {project.date}, priority {project.priority},"
              f" estimate: ${project.cost}, completion: {project.percentage}%")
    print("Completed projects:")
    for project in complete_projects:
        print(f"\t{project.name}, start: {project.date}, priority {project.priority},"
              f" estimate: ${project.cost}, completion: {project.percentage}%")


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
