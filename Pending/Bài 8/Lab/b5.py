from datetime import datetime

# initialize current time
now = datetime.now()

# print desired values
print(f"Today is {now.strftime('%d/%m/%Y')}")
print(f"Time right now: {now.strftime('%H:%M:%S')}")