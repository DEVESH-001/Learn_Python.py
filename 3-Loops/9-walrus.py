# walrus: The walrus operator (:=) allows you to assign a value to a variable AND use it in an expression at the same time.

# syntax: var := expression

# value = 10

# remainder = value % 5 

# if remainder == 0:
#     print(f"{value} is divisible by 5")

value = 13 
if (remainder := value % 5):
    print(f"{value} is not divisible by 5, remainder is {remainder}")

available_sizes = ["S", "M", "L", "XL", "XXL"]
if (requested_size := input("Enter Size: ")) in available_sizes:
    print(f"Size {requested_size} is available")

flavours = ["Ginger", "mint", "lemon", "Tulsi", "Coco"]

print("Available flavours are: ", flavours)

while(flavour := input("Enter flavour: ")) not in flavours: # not in flavours : keep asking until a valid flavour is entered
    print("Flavour not available")
print(f"Enjoy your {flavour} tea")