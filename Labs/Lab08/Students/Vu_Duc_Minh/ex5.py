from datetime import datetime
now = datetime.now()
now1 = now.strftime('%d/%m/%Y')
now2 = now.strftime('%H:%M:%S')
print(f'Today is: {now1}')
print(f'Time right now: {now2}')