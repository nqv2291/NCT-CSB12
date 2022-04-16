from datetime import datetime
now=datetime.now()
print(f"Today is {now.strftime('%Y/%m/%d')}")
print(f"The time now is {now.strftime('%H:%M:%S')}")