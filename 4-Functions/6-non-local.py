# nonlocal keyword allows you to modify a variable in the enclosing (non-global) scope.

def update_order():
    chai_type = "Elachi Chai"  # Enclosing Scope
    def kitchen():
        nonlocal chai_type
        chai_type = "Ginger Chai"  # Modifying Enclosing Scope
    kitchen()
    print(f"After updating, order is: {chai_type}")  # Accessing Enclosing Scope

update_order()