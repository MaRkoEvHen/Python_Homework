get_number = int(input("Enter a number from 0 to 8640000: "))
if 0 <= get_number <= 8640000:
    days = get_number // 86400
    rem_sec = get_number % 86400
    hours = rem_sec // 3600
    minutes = (rem_sec % 3600) // 60
    seconds = rem_sec % 60
    if days == 1:
        days_str = "день"
    elif days % 10 == 1 and days % 100 != 11:
        days_str = "день"
    elif 2 <= days % 10 <= 4 and (days % 100 < 10 or days % 100 > 20):
        days_str = "дні"
    else:
        days_str = "днів"


    hours_str = str(hours).zfill(2)
    minutes_str = str(minutes).zfill(2)
    seconds_str = str(seconds).zfill(2)
    print(f"{days} {days_str}, {hours_str}:{minutes_str}:{seconds_str}")
