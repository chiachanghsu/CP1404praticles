from prac_09.taxi import Taxi
from prac_09.silver_service_taxi import SilverServiceTaxi

MENU = 'Q)uit, C)hoose taxi, D)rive'
TAXIS = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]


def main():
    total_cost = 0
    print(f"Let's drive!\n{MENU}")
    choice = input('>>> ').upper()
    current_taxi = None
    while choice != 'Q':
        if choice == 'C':
            current_taxi = choose_taxi()
        elif choice == 'D':
            cost = drive(current_taxi)
            total_cost += cost
        else:
            print('Invalid option')
        print(f'Bill to date: ${total_cost:.2f}')
        print(MENU)
        choice = input('>>> ').upper()
    print(f'Total trip cost: ${total_cost:.2f}')
    for i, taxi in enumerate(TAXIS, 0):
        print(f'{i} - {taxi}')


def choose_taxi():
    print("Taxis available:")
    for i, taxi in enumerate(TAXIS, 0):
        print(f'{i} - {taxi}')
    is_valid = False
    while not is_valid:
        try:
            taxi_choice = int(input('>>> '))
            if not 0 <= taxi_choice <= len(TAXIS) - 1:
                print('Invalid taxi choice')
            else:
                is_valid = True
        except ValueError:
            print('Invalid taxi choice')
    return TAXIS[taxi_choice]


def drive(current_taxi):
    cost = 0
    if current_taxi is None:
        print('You need to choose a taxi before you can drive.')
    else:
        if current_taxi.fuel == 0:
            print('The fuel is empty.')
        else:
            current_taxi.start_fare()
            is_valid = False
            while not is_valid:
                try:
                    distance = int(input('Drive how far? '))
                    if distance <= 0:
                        print('Invalid distance.')
                    else:
                        is_valid = True
                except ValueError:
                    print('Invalid distance.')
            current_taxi.drive(distance)
            cost = current_taxi.get_fare()
            print(cost)
            print(f'Your Prius trip cost you ${cost:.2f}')
    return cost


main()
