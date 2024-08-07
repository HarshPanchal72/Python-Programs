import datetime
import calendar

def get_month_details(month_name):
    month_names = [month for month in calendar.month_name if month]
    month_index = month_names.index(month_name.capitalize()) + 1  # Add 1 to the index
    year = datetime.datetime.today().year

    total_days = calendar.monthrange(year, month_index)[1]

    weekdays = 0
    weekends = 0

    for day in range(1, total_days + 1):
        date = datetime.date(year, month_index, day)
        if date.weekday() < 5: 
            weekdays += 1
        else:
            weekends += 1

    print(f'Month: {month_name.capitalize()} {year}')
    print(f'Total days: {total_days}')
    print(f'Total weekdays: {weekdays}')
    print(f'Total weekends: {weekends}')
    print(datetime.datetime.today().time())

month_name = input("Enter the month name (e.g. January, February, ...): ")
get_month_details(month_name)