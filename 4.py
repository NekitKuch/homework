# Task 4
from datetime import datetime, timedelta

def get_upcoming_birthdays(users):
    today = datetime.today().date()
    upcoming_birthdays = []

    for user in users:
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()

        if birthday < today:
            birthday = birthday.replace(year=today.year + 1)

        birthday_this_year = birthday.replace(year=today.year)

        days_until_birthday = (birthday_this_year - today).days

        if 0 <= days_until_birthday < 8:
            congratulation_date = birthday_this_year
            if congratulation_date.weekday() >= 5:  
                days_until_monday = (7 - congratulation_date.weekday()) + 1
                congratulation_date += timedelta(days=days_until_monday)

            upcoming_birthdays.append({
                "name": user["name"],
                "congratulation_date": congratulation_date.strftime("%Y.%m.%d")
            })

    return upcoming_birthdays

users = [
    {"name": "John Doe", "birthday": "2024.02.03"},
    {"name": "Jane Smith", "birthday": "2024.02.06"}
]

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)
