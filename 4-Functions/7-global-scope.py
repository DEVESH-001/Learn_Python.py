# global variable can be accessed inside functions, but to modify it, use the 'global' keyword.

chai_type = "Masala Chai"  # Global Scope

def serve_chain():
    def kitchen():
        global chai_type
        chai_type = "Cardamom Chai"  # Modifying Global Scope
    kitchen()

serve_chain()
print(f"Final serving, chai type is: {chai_type}")  # Accessing Global Scope