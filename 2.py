# Task 2
import random

def get_numbers_ticket(min, max, quantity):
    if not (isinstance(min, int) and isinstance(max, int) and isinstance(quantity, int)):
        return []

    if not (0 <= min <= max):
        return []

    num_set = set()
    while len(num_set) < quantity:
        num_set.add(random.randint(min, max))

    return sorted(list(num_set))

try:
    lottery_numbers = get_numbers_ticket(1, 60, 6)
    print("Ваші лотерейні числа:", lottery_numbers)
except ValueError:
    print("Неправильні параметри для генерації лотерейних чисел.")
