from datetime import datetime

def calculate_age_in_detail(birthdate):
    today = datetime.today()
    age_years = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    age_months = age_years * 12 + today.month - birthdate.month - (today.day < birthdate.day)
    past_birthdate_this_year = datetime(today.year, birthdate.month, birthdate.day)
    if today < past_birthdate_this_year:
        past_birthdate_this_year = datetime(today.year - 1, birthdate.month, birthdate.day)
    age_days = (today - past_birthdate_this_year).days + age_years * 365 + sum(1 for year in range(today.year - age_years, today.year) if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0))
    age_hours = age_days * 24

    return age_years, age_months, age_days, age_hours

def main():
    # Запрашиваем у пользователя имя и дату рождения
    name = input("Введите ваше имя: ")
    print("Введите вашу дату рождения (дд.мм.гггг): ")
    birthdate_input = input()
    birthdate = datetime.strptime(birthdate_input, "%d.%m.%Y")

    # Рассчитываем возраст в годах, месяцах, днях, часах
    age_years, age_months, age_days, age_hours = calculate_age_in_detail(birthdate)

    # Выводим информацию
    print(f"Привет {name}! Тебе {age_years} лет.")
    print(f"Ты прожил(а): {age_months} месяцев, {age_days} дней, {age_hours} часов.")

#Вызов  основной функции
main()
