from prac_07.project import Project
import datetime

MENU = (" - (L)oad projects\n - (S)ave projects\n - (D)isplay projects\n"
        " - (F)ilter projects by date\n - (A)dd new project\n - (U)pdate project\n - (Q)uit")
HEADING = "Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage"
YES_NO = ["Y", "YES", "N", "NO"]
STARTING_VALUE = 0
ENDING_VALUE = 100
DATE_END_VALUE = 32
MONTH_END_VALUE = 12
YEAR_LENGTH = 4
DATE_LENGTH = 3
INDEX_OF_DAY = 0
INDEX_OF_MONTH = 1
INDEX_OF_YEAR = 2


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
            question = "Show projects that start after date (dd/mm/yy): "
            date_to_compare = get_valid_date(question)
            datas = compare_date(texts, date_to_compare)
            for data in datas:
                print(f"\t{data.name}, start: {data.date}, "
                      f"priority {data.priority},"f" estimate: ${data.cost}, "
                      f"completion: {data.percentage}%")
        elif choice == "A":
            print("Let's add a new project.")
            name = get_valid_name()
            question = "Start date (dd/mm/yy): "
            date = get_valid_date(question)
            cost, percentage, priority = get_valid_number()
            texts.append(Project(name, date, priority, cost, percentage))
        elif choice == "U":
            update_project(texts)
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


def compare_date(texts, date_to_compare):
    datas = []
    date_string = date_to_compare
    date_to_compare = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
    for text in texts:
        date_string = text.date
        date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
        if date >= date_to_compare:
            datas.append(text)
    return datas


def update_project(texts):
    count = STARTING_VALUE
    for i, text in enumerate(texts):
        count += 1
        print(f"{i}\t{text.name}, start: {text.date}, priority {text.priority},"
              f" estimate: ${text.cost}, completion: {text.percentage}%")
    project_choice = int(input("Project choice: "))
    while not STARTING_VALUE <= project_choice < count:
        print("Invalid input.")
        project_choice = int(input("Project choice: "))
    print(f"\t{texts[project_choice].name}, start: {texts[project_choice].date}, "
          f"priority {texts[project_choice].priority},"f" estimate: ${texts[project_choice].cost}, "
          f"completion: {texts[project_choice].percentage}%")
    new_percentage = int(input("New project percentage: "))
    while not STARTING_VALUE <= new_percentage <= ENDING_VALUE:
        print("Invalid input.")
        new_percentage = int(input("New project percentage: "))
    texts[project_choice].percentage = new_percentage
    new_priority = int(input("New project priority: "))
    while not STARTING_VALUE < new_priority:
        print("Invalid input.")
        new_priority = int(input("New project priority: "))
    texts[project_choice].priority = new_priority


def get_valid_number():
    try:
        priority = int(input("Priority: "))
        while priority < STARTING_VALUE:
            print("Invalid input.")
            priority = int(input("Priority: "))
        priority = str(priority)
        cost = float(input("Cost estimate: $"))
        while cost < STARTING_VALUE:
            print("Invalid input.")
            cost = float(input("Cost estimate: $"))
        percentage = int(input("Percentage: "))
        while not STARTING_VALUE <= percentage <= ENDING_VALUE:
            print("Invalid input.")
            percentage = int(input("Percentage: "))
    except ValueError:
        print("Invalid input.")
    return cost, percentage, priority


def get_valid_date(question):
    is_valid = False
    while not is_valid:
        date = input(question)
        date = date.split("/")
        if len(date) != DATE_LENGTH:
            print("Invalid date.")
        else:
            day = date[INDEX_OF_DAY]
            month = date[INDEX_OF_MONTH]
            year = date[INDEX_OF_YEAR]
            if STARTING_VALUE < int(day) < DATE_END_VALUE and STARTING_VALUE < int(month) < MONTH_END_VALUE and len(year) < YEAR_LENGTH:
                print("Invalid date.")
            else:
                is_valid = True
    date = day + "/" + month + "/" + year
    return date


def get_valid_name():
    name = input("Name: ").title()
    while name == '':
        print("Invalid input.")
        name = input("Name: ").title()
    return name


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


main()
