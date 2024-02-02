# Task 2
import random

def get_numbers_ticket(min, max, quantity):
    num_set = set()
    while len(num_set) < quantity:
        num_set.add(random.randint(min, max))
    
    return sorted(list(num_set))

lottery_numbers = get_numbers_ticket(1, 60, 6)
print("Ваші лотерейні числа:", lottery_numbers)