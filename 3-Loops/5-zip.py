# Zip : Looping through multiple iterables
# syntax : zip(*iterables)

names = ['Devesh','Alice','Bob']
bills = [250,300,400]

for name, amount in zip(names,bills):
    print(f"{name} paid {amount} rupees")
