# input params : function with input parameters

# chai = "Masala Chai"  # Global Scope

# def prepare_chai(order):
#     print(f"Preparing your {order}")
    
# prepare_chai("Ginger Chai")  # Passing argument to function
# print(chai)  # Passing global variable as argument


chai = [1,2,3] # list in global scope

def edit_chai(cup):
    cup[1] = 99  # Modifying the second element

edit_chai(chai)
print(chai)

def make_chai(tea,milk,sugar):
    print(f"Making chai with {tea}, {milk}, and {sugar}")

make_chai("Masala Chai","Full Cream Milk","Less Sugar")
# Using keyword arguments
make_chai(tea="Green Tea",sugar="Less Sugar",milk="Full Cream Milk")

# arguments & key value arguments can be combined
def special_chai(*ingredients, **extras):
    print("Ingredients", ingredients)
    print("Extras", extras)

special_chai("Cinnamon","Green Tea",sweetener="Honey",foam="Yes")

# def chai_order(order=[]):
#     order.append("Masala Chai hi de d")
#     print(order)

# chai_order()  # First call
# chai_order()  # Second call, demonstrates mutable default argument issue


# Correct way to handle mutable default arguments
def chai_order(order=None):
    if order is None:
        order = [] # create a new list if none is provided
    order.append("Masala Chai hi de d")
    print(order)

chai_order()  
chai_order() 