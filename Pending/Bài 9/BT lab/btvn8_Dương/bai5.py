from datetime import datetime
now = datetime.now()
print(now)

print(f"Today is {now.day}/{now.month}/{now.year}")
print(f"Time right now: {now.hour}:{now.minute}:{now.second}")