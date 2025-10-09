from datetime import datetime

def drop_microseconds(input_datetime):
    result_datetime = input_datetime.replace(microsecond=0)
    return result_datetime

current_datetime = datetime.now()
datetime_without_microseconds = drop_microseconds(current_datetime)

print("Original datetime:", current_datetime)
print("Datetime without microseconds:", datetime_without_microseconds)
