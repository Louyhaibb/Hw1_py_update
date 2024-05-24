import datetime
import random

def rand_date(start, end):
    s_date = datetime.datetime.strptime(start, "%Y-%m-%d")
    e_date = datetime.datetime.strptime(end, "%Y-%m-%d")

    time_between_dates = e_date - s_date
    days_between_dates = time_between_dates.days
    random_numb_of_days = random.randrange(days_between_dates)
    rand_date = s_date + datetime.timedelta(days=random_numb_of_days)

    return rand_date

def print_date_with_message(random_date):
    if random_date.weekday() == 0:
        print(f"The random date is {random_date.strftime('%Y-%m-%d')} -no vinnigrete!")
    else:
        print(f"The random date is {random_date.strftime('%Y-%m-%d')}")

if __name__ == '__main__':
    start_date_in = input("Enter the start date (YYYY-MM-DD): ")
    end_date_in = input("Enter the end date (YYYY-MM-DD): ")
    random_date = rand_date(start_date_in, end_date_in)
    print_date_with_message(random_date)
