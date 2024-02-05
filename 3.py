import re

def normalize_phone(phone_number):
    # прибираємо мусор в номері
    cleaned_number = re.sub(r"[^0-9+]", "", phone_number)

    # якщо є +, але немає 380, нічого не змінюємо
    if cleaned_number.startswith('+') and not cleaned_number.startswith('+380'):
        return cleaned_number

    # додаємо +380, якщо його немає
    if not cleaned_number.startswith('+') and not cleaned_number.startswith('380'):
        # якщо нуль на початку
        cleaned_number = '+380' + cleaned_number.lstrip('0')
    elif cleaned_number.startswith('380') and len(cleaned_number) > 12:
        # коли є +380
        cleaned_number = '+' + cleaned_number[3:]
    elif cleaned_number.startswith('380') and len(cleaned_number) == 12:
        # якщо є 380, але немає +
        cleaned_number = '+' + cleaned_number

    return cleaned_number

raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "+123456789012 ",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
    "0601234567",
    "+123456789",  
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)
