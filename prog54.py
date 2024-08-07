# python code for list of month names starting with current month.
import datetime 
from datetime import time
import calendar

current_month = datetime.datetime.now().month



list_of_months = calendar.month_name[1:]

clock = datetime.datetime.now()
current_index = current_month - 1
list_of_months = list_of_months[current_index:] + list_of_months[:current_index]

print(list_of_months,clock)
