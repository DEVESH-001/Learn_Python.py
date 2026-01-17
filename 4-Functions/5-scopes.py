# # Scopes: A variable is only available from inside the region it is created. This is called scope.

# def serve_coffee():
#     coffee_type = "Latte"  # Local Scope
#     print(f"Inside function {coffee_type}")

# coffee_type = "Espresso"  # Global Scope
# serve_coffee()
# print(f"Outside function: {coffee_type}") # Accessing Global Scope, outside the function

# Enclosing Scope : A variable in the local scope of an enclosing function is accessible to a nested function.

def coffee_counter():
    coffee_order = "Cappuccino"  # Enclosing Scope
    def print_order():
        coffee_order = "Mocha"  # Local Scope
        print(f"Inner nested function: {coffee_order}")  # Accessing Enclosing Scope
    print_order()
    print(f"Outer outer function: {coffee_order}")  # Accessing Enclosing Scope

coffee_counter()

coffee_order = "Americano"  # Global Scope
coffee_counter() # Accessing Global Scope, outside the function
print(f"Global scope: {coffee_order}")  # Accessing Global Scope