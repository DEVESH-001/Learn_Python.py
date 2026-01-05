is_boiling = True
no_of_ingredients = 4
total_actions = is_boiling + no_of_ingredients #upcasting boolean to integer
print(f"Total_actions:{total_actions}")

milk_present = 0 #no milk
print(f"Is there milk?:{bool(milk_present)}") #downcasting integer to boolean

tea_ready = None
print(f"Is tea ready?:{bool(tea_ready)}") #None is considered as False


## Logical Operators -> and, or, not

water_hot = True
tea_added = False

can_server = water_hot and tea_added
print(f"Can we serve chai?:{can_server}")