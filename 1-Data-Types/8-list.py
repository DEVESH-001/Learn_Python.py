# List : Mutable ordered collections, defined using square brackets []
# Lists can hold elements of different data types and support various operations like indexing, slicing, appending, and removing elements.

ai_tools = ["ChatGPT", "Claude", "Gemini"]  # List literal
ai_tools.append("Meta") # Adding an element to the list
print(f"AI Tools: {ai_tools}")

ai_tools.remove("Gemini") # Removing an element from the list
print(f"After Removal: {ai_tools}")

spice_options = ["ginger", "cardamom", "cinnamon", "cloves"]
coffee_ingredients = ["coffee beans", "water", "milk"]

coffee_ingredients.extend(spice_options) # Extending list with another list
print(f"Coffee Ingredients with Spices: {coffee_ingredients}")

coffee_ingredients.insert(1, "sugar") # Inserting an element at a specific position
print(f"After Inserting Sugar: {coffee_ingredients}")

last_added = coffee_ingredients.pop() # Removing and returning the last element
print(f"Last Added Ingredient Removed: {last_added}")
print(f"Final Coffee Ingredients: {coffee_ingredients}")

coffee_ingredients.reverse() # Reversing the list
print(f"Reversed Coffee Ingredients: {coffee_ingredients}")

coffee_ingredients.sort() # Sorting the list
print(f"Sorted Coffee Ingredients: {coffee_ingredients}")

coffee_level = [1,2,3,4,5]
max_level = max(coffee_level) # Finding maximum value in the list
min_level = min(coffee_level) # Finding minimum value in the list
print(f"Max Coffee Level: {max_level}, Min Coffee Level: {min_level}")



# # Slicing: Extracting a sublist
# selected_spices = spice_options[1:3] # Extracting "cardamom"
# print(f"Selected Spices: {selected_spices}")