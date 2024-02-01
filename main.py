# Task 1
# from datetime import datetime, timedelta

# def get_days_from_today(date): 
#     input_date = datetime.strptime(date, "%Y-%m-%d") 
#     current_date = datetime.today() 
#     days = (current_date - input_date).days 
#     return days

# result = get_days_from_today(input("Введіть дату у форматі 'РРРР-ММ-ДД': "))
# print(result)



# Task 2
# import random

# def get_numbers_ticket(min, max, quantity):
#     num_set = set()
#     while len(num_set) < quantity:
#         num_set.add(random.randint(min, max))
    
#     return sorted(list(num_set))

# lottery_numbers = get_numbers_ticket(1, 60, 6)
# print("Ваші лотерейні числа:", lottery_numbers)



# Task 3
# import re

# def normalize_phone(phone_number):

#     cleaned_number = re.sub(r'\D', '', phone_number)

#     if not cleaned_number.startswith('+'):
#         cleaned_number = '+38' + cleaned_number

#     return cleaned_number

# raw_numbers = [
#     "067\\t123 4567",
#     "(095) 234-5678\\n",
#     "+380 44 123 4567",
#     "380501234567",
#     "    +38(050)123-32-34",
#     "     0503451234",
#     "(050)8889900",
#     "38050-111-22-22",
#     "38050 111 22 11   ",
# ]

# sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
# print("Нормалізовані номери телефонів:", sanitized_numbers)



# Task 4
# from datetime import datetime, timedelta

# def get_upcoming_birthdays(users):
#     today = datetime.today().date()
#     upcoming_birthdays = []

#     for user in users:
#         birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()

#         birthday_this_year = birthday.replace(year=today.year)

#         days_until_birthday = (birthday_this_year - today).days

#         if 0 <= days_until_birthday < 8:
#             congratulation_date = birthday_this_year
#             if congratulation_date.weekday() >= 5:  
#                 days_until_monday = (7 - congratulation_date.weekday()) + 1
#                 congratulation_date += timedelta(days=days_until_monday)

#             upcoming_birthdays.append({
#                 "name": user["name"],
#                 "congratulation_date": congratulation_date.strftime("%Y.%m.%d")
#             })

#     return upcoming_birthdays

# users = [
#     {"name": "John Doe", "birthday": "2024.02.3"},
#     {"name": "Jane Smith", "birthday": "2024.02.6"}
# ]

# upcoming_birthdays = get_upcoming_birthdays(users)
# print("Список привітань на цьому тижні:", upcoming_birthdays)






