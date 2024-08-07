import datetime
import calendar

month_name = input('Enter a month name : ') #get name of month

month_number = list(calendar.month_name).index(month_name) #get the index of current month

current_year = datetime.datetime.now().year #get current year

total_days = calendar.monthrange(current_year, month_number)[1] #count total days of month

weekdays = sum(1 for day in range(1, total_days + 1) 
               if datetime.date(current_year, month_number, day).weekday() < 5)
off_days = total_days - weekdays    

print(f'Total days in {month_name} : {total_days}')
print(f'Weekdays in {month_name} : {weekdays}')
print(f'Off days (weekends) in {month_name} : {off_days}')