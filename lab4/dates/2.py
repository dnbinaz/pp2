from datetime import datetime, timedelta

yesterday = datetime.now() - timedelta(days=1)
tomorrow = datetime.now() + timedelta(days=1)

print("Yesterday: ", yesterday.strftime("%Y-%m-%d"))
print("Today: ", datetime.now().strftime("%Y-%m-%d"))
print("Tomorrow: ", tomorrow.strftime("%Y-%m-%d"))