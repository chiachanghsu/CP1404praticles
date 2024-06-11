import random
MINIMUM_NUMBER = 1
MAXIMUM_NUMBER = 45
NUMBER_CHOOSE = 6


quick_picks = int(input("How many quick picks? "))
for i in range(quick_picks):
    pick_list = []
    for v in range(NUMBER_CHOOSE):
        pick = random.randint(MINIMUM_NUMBER, MAXIMUM_NUMBER)
        while pick in pick_list:
            pick = random.randint(MINIMUM_NUMBER, MAXIMUM_NUMBER)
        pick_list.append(pick)
    pick_list.sort()
    print(pick_list)

