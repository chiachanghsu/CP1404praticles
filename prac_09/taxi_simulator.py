from prac_09.taxi import Taxi
from prac_09.silver_service_taxi import SilverServiceTaxi
MENU = 'Q)uit, C)hoose taxi, D)rive'


def main():
    print("Let's drive!\nMENU")
    choice = input('>>> ').upper()
    while choice != 'Q':
        if choice == 'C':
            taxi_choice = choose_taxi()
            print(taxi_choice)
        elif choice == 'D':
            print('Drive')
        else:
            print('Invalid option')
        choice = input('>>> ').upper()
    print('Total trip cost:')


def choose_taxi():
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    print("Taxis available:")
    for i, taxi in enumerate(taxis, 0):
        print(f'{i} - {taxi}')
    is_valid = False
    while not is_valid:
        try:
            taxi_choice = int(input('>>> '))
            if not 0 <= taxi_choice <= len(taxis) - 1:
                print('Invalid taxi choice')
            else:
                is_valid = True
        except ValueError:
            print('Invalid taxi choice')
    return taxis[taxi_choice]


main()
