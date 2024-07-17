from prac_06.guitar import Guitar

# Gibson L-5 CES get_age() - Expected 100. Got 100
# Another Guitar get_age() - Expected 9. Got 9
# Gibson L-5 CES is_vintage() - Expected True. Got True
# Another Guitar is_vintage() - Expected False. Got False
guitars = [Guitar(name="Gibson L-5 CES", year=1922, cost=16035.40),
           Guitar(name="Another guitar", year=1972, cost=1020)]
for guitar in guitars:
    print(guitar.get_age(), guitar.is_vintage())

