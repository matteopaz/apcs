
groceries = ["cheez its", "nerds gummy clusters", "doritos", "cocoa puffs", "pepsi", "dr. pepper", "mountain dew"]

while True:
    rem = input("What do I remove? ").lower()
    if rem == "stop":
        break
    groceries.remove(rem)
    
print("Final cart: ", groceries)


    