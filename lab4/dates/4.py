from datetime import datetime

def get_user_input():
    date1_str = input("Enter date 1 (YYYY-MM-DD HH:MM:SS): ")
    date1 = datetime.strptime(date1_str, "%Y-%m-%d %H:%M:%S")
    date2_str = input("Enter date 2 (YYYY-MM-DD HH:MM:SS): ")
    date2 = datetime.strptime(date2_str, "%Y-%m-%d %H:%M:%S")
    return date1, date2

def date_difference_in_seconds(date1, date2):
    time_difference = date2 - date1
    seconds_difference = time_difference.total_seconds()
    return seconds_difference

user_date1, user_date2 = get_user_input()
difference_in_seconds = date_difference_in_seconds(user_date1, user_date2)

print("Date 1:", user_date1)
print("Date 2:", user_date2)
print("Difference in seconds:", difference_in_seconds)
#2022-01-01 12:00:00
#2022-01-02 18:30:45
#109845.0
