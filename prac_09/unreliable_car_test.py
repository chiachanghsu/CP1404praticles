import random
from prac_09.unreliable_car import UnreliableCar
STARTING_VALUE = 0
ENDING_VALUE = 100
DRIVING_VALUE = 40


my_car = UnreliableCar("Prius 2", 100, 50.0)
# print(my_car)
if random.randint(STARTING_VALUE, ENDING_VALUE) < my_car.reliability:
    my_car.drive(DRIVING_VALUE)
print(my_car)
