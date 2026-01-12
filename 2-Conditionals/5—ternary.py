order_amount = int(input("Enter the order amount: "))

#print(f"Order amount: {type(order_amount)}")

# ternary operation
delivery_fees = 0 if order_amount > 300 else 30 # If order amount is greater than 300, delivery fees is 0, else it is 30
print(f"Delivery Fees: {delivery_fees}")

# Nested ternary operation
delivery_fees = 0 if order_amount > 300 else 10 if order_amount > 150 else 30
print(f"Delivery Fees (nested): {delivery_fees}")



