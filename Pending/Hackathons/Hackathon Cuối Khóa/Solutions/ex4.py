# initialize order list
orders = []

print('\n= Welcome to MindX Restaurant ==')

# getting orders
while True:
  
  # Step 1: Ask customer to choose a dish
  print('\nPlease choose a dish: ', end='')
  dish = input()

  # Step 2: Check if dish already in order
  if dish not in orders:  # if not in order => add to orders
    orders.append(dish)
    print('Great choice! ', end='')
  else:                   # if already in order => notify
    print('You chose this already. ', end='')

  # Step 3: Ask if customer wants to proceed
  print('Anything else? (y/n): ', end='')
  choice = input()
  if choice == 'n':  # if not proceed => end the loop
    break

# summarize order
print('\nWell done! Your order:')
for dish in orders:
  print('-', dish)