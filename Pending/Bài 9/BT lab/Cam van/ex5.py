from datetime import datetime
now = datetime.now()

print("Today is", now.strftime('%d/%m/%Y'))
print("Time right now:", now.strftime('%H:%M:%S'))