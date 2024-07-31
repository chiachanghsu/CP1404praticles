from prac_09.car import Car
from prac_09.silver_service_taxi import SilverServiceTaxi
MENU = 'Q)uit, C)hoose taxi, D)rive'


def main():
    print("Let's drive!\nMENU")
    choice = input('>>> ').upper()
    while choice != 'Q':
        if choice == 'C':
            print('Choose taxi')
        elif choice == 'D':
            print('Drive')
        else:
            print('Invalid option')
        choice = input('>>> ').upper()
    print('Total trip cost:')


main()
