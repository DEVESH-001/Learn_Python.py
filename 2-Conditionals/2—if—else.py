# to take input we use input
snack = input("Enter your snack:").lower()
#print(f"User said:{snack}")


if snack == "cookies" or snack == "samosa":
    print(f"Great Choice ! : {snack}")
else:
    print("Sorry its out of stock")
