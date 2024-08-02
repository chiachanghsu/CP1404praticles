from prac_09.taxi import Taxi

my_taxi = Taxi("Prius 1", 100)
my_taxi.drive(40)
print(my_taxi)   # Prius 1, fuel=60, odometer=40, 40km on current fare, $1.23/km
my_taxi.start_fare()
my_taxi.drive(100)
print(my_taxi)   # Prius 1, fuel=0, odometer=100, 60km on current fare, $1.23/km

