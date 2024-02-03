# Task 1
from datetime import datetime, timedelta

def get_days_from_today(date_str): 
    try:
        input_date = datetime.strptime(date_str, "%Y-%m-%d") 
    except ValueError:
        return "Неправильний формат дати. Введіть у форматі 'РРРР-ММ-ДД'."

    current_date = datetime.today() 
    days = (current_date - input_date).days 
    return days

user_input = input("Введіть дату у форматі 'РРРР-ММ-ДД': ")
result = get_days_from_today(user_input)
print(result)
