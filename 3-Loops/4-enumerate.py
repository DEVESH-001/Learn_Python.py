# Enumerate : Looping with index
# syntax : enumerate(iterable, start=0)

menu = ['espresso', 'cappuccino', 'latte', 'mocha']

for index, item in enumerate(menu, start=1):        #start index from 1,  default is 0
    print(f"Menu item {index} : {item}")
