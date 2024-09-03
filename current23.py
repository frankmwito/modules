# type: ignore # use datetime module to print the current date and time in a specific format

from datetime import datetime


def current():
    current_date = datetime.now()
    
    formatterd_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    return formatterd_date

print(current())