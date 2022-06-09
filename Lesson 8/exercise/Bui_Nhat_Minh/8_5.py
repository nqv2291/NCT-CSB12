from datetime import datetime
now = datetime.now()
print(f"Today is {now.strftime('%Y/%m/%d')}")
print(f"Time right now: {now.strftime('%H:%M:%S')}")
