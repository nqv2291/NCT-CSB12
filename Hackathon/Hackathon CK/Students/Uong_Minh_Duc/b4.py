foodlist={
    
}
def confirm():
    checker=input("Great choice! Anything else? (y/n):")
    if checker == "y":
        return True
    else:
        return False
print("== Welcome to MindX Restaurant ==")
while True:
    new_food=input("choose a dish:")
    confirm()
    
