# Dictionary : A dictionary is a collection of key-value pairs. Each key is unique and is used to store and retrieve values.
# Dictionaries are defined using curly braces {} with key-value pairs separated by colons (:).
# how it works: You can access, add, remove, and modify values in a dictionary using their corresponding keys.

coffee_menu = dict(type="Latte", size="Medium", price=4.5)
print("Initial Coffee Menu:", coffee_menu)

coffee_recipe = {} # Empty dictionary
coffee_recipe["Espresso Shots"] = 2 # Adding key-value pair(data)
coffee_recipe["Milk"] = "160ml" # Adding key-value pair(data)

print("Coffee Recipe after additions:", coffee_recipe)

del coffee_recipe["Milk"] # Removing key-value pair(data)
print("Coffee Recipe after deletion:", coffee_recipe)

print("Is milk in the coffee recipe?",{"Milk" in coffee_recipe})

new_coffee_menu={"type": "Cappuccino", "size": "Large", "price": 70}
# print(f"New Coffee Menu (keys): {new_coffee_menu.keys()}")
# print(f"New Coffee Menu (values): {new_coffee_menu.values()}")
# print(f"New Coffee Menu (items): {new_coffee_menu.items()}")

last_item = new_coffee_menu.popitem() # removes and returns the last inserted key-value pair
print(f"Last item removed from new coffee menu: {last_item}")

coffee_brands = {"Starbucks": ["Espresso", "Latte", "Cappuccino"]}
                # "Dunkin": ["Americano", "Mocha", "Macchiato"],
                # "Costa": ["Flat White", "Cortado", "Ristretto"]}

coffee_menu.update(coffee_brands) # Merging two dictionaries
print("Updated Coffee Menu with Brands:", coffee_menu)

coffee_size  = coffee_menu["size"] # Accessing value using key
coffee_size  = coffee_menu.get("note","no Note") # Accessing value using get() method (returns None if key not found)
print(f"Coffee Size: {coffee_size}")