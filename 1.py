# Task 1
from datetime import datetime, timedelta

def get_days_from_today(date): 
    input_date = datetime.strptime(date, "%Y-%m-%d") 
    current_date = datetime.today() 
    days = (current_date - input_date).days 
    return days

result = get_days_from_today(input("Введіть дату у форматі 'РРРР-ММ-ДД': "))
print(result)