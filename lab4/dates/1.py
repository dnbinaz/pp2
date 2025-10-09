from datetime import datetime, timedelta

new_date = datetime.now() - timedelta(days=5)

print("Current Date:", datetime.now().strftime("%Y-%m-%d"))
print("New Date (after subtracting 5 days):", new_date.strftime("%Y-%m-%d"))