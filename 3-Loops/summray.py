# ============================================
# PYTHON LOOPS - COMPLETE SUMMARY
# ============================================

# ============================================
# 1. RANGE - Generate Sequence of Numbers
# ============================================
# Syntax: range(start, stop, step)
# Usage: Generate numbers for iteration

# Example:
for token in range(1, 11):
    print(token)  # Prints 1 to 10

for token2 in range(0, 21):
    print(token2)  # Prints 0 to 20


# ============================================
# 2. FOR LOOP BASICS
# ============================================
# Basic for loop iteration

# Example: Print numbers 1 to 4
for chai_in_range in range(1, 5):
    print(chai_in_range)


# ============================================
# 3. LOOPING THROUGH LISTS
# ============================================
# Iterate through list items

# Example: Process customer orders
customers = ["Devesh", "Neelesh", "Akshat"]

for order in customers:
    print("Order for " + order)


# ============================================
# 4. ENUMERATE - Looping with Index
# ============================================
# Syntax: enumerate(iterable, start=0)
# Usage: Get both index and value while looping

# Example: Menu with item numbers
menu = ['espresso', 'cappuccino', 'latte', 'mocha']

for index, item in enumerate(menu, start=1):  # Start index from 1
    print(f"Menu item {index} : {item}")


# ============================================
# 5. ZIP - Looping Through Multiple Iterables
# ============================================
# Syntax: zip(*iterables)
# Usage: Loop through multiple lists simultaneously

# Example: Match names with bills
names = ['Devesh', 'Alice', 'Bob']
bills = [250, 300, 400]

for name, amount in zip(names, bills):
    print(f"{name} paid {amount} rupees")


# ============================================
# 6. WHILE LOOP - Condition-Based Iteration
# ============================================
# Syntax: while condition:
# Usage: Repeat as long as condition is true

# Example: Heat tea until temperature reaches 100
temperature = 40

while temperature < 100:
    print(f"Current temp : {temperature}")
    temperature += 15

print("tea is ready")


# ============================================
# 7. SKIP & BREAK (continue & break)
# ============================================
# continue: Skip to next iteration
# break: Exit the loop immediately

# Example: Process flavours, skip/break on conditions
flavours = ["Ginger", "Out of stock", "lemon", "discontinue", "Tulsi", "Coco"]

for flavour in flavours:
    if flavour == "Out of stock":
        continue  # Skip this iteration
    if flavour == "discontinue":
        print(f"{flavour} item found")
        break  # Exit loop
    print(f"{flavour} item found")

print("Outside of loop")


# ============================================
# 8. FOR-ELSE - Loop with Else Block
# ============================================
# The else block executes only if loop completes normally
# (without encountering a break statement)

# Example: Find eligible staff member
staff = [("Devesh", 24), ("Ankita", 22), ("Ravi", 28), ("Sneha", 26)]

for name, age in staff:
    if age <= 30:
        print(f"{name}")
        break
else:
    print("No one is eligible")  # Only runs if no break occurred


# ============================================
# 9. WALRUS OPERATOR (:=)
# ============================================
# Syntax: var := expression
# Usage: Assign AND use value in same expression

# Example 1: Check remainder
value = 13
if (remainder := value % 5):
    print(f"{value} is not divisible by 5, remainder is {remainder}")

# Example 2: Validate input in condition
available_sizes = ["S", "M", "L", "XL", "XXL"]
if (requested_size := input("Enter Size: ")) in available_sizes:
    print(f"Size {requested_size} is available")

# Example 3: Validate input in loop
flavours = ["Ginger", "mint", "lemon", "Tulsi", "Coco"]

print("Available flavours are: ", flavours)

# Keep asking until valid flavour entered
while (flavour := input("Enter flavour: ")) not in flavours:
    print("Flavour not available")
print(f"Enjoy your {flavour} tea")


# ============================================
# 10. DICTIONARY ITERATION
# ============================================
# Working with dictionaries in loops

# Example: Apply coupons and calculate discounts
users = [
    {"id": 1, "total": 100, "coupon": "P20"},
    {"id": 2, "total": 200, "coupon": "X15"},
    {"id": 3, "total": 300, "coupon": "F50"},
]

# Dictionary of discounts (percentage, fixed amount)
discounts = {
    "P20": (0.2, 0),  # 20% discount
    "X15": (0.5, 0),  # 50% discount
    "F50": (0.8, 0),  # 80% discount
}

for u in users:
    percent, fixed = discounts.get(u["coupon"], (0, 0))
    discount = u["total"] * percent + fixed
    print(f"{u['id']} paid {u['total'] - discount} Discount: {discount}")


# ============================================
# KEY CONCEPTS SUMMARY
# ============================================
# - range(): Generate number sequences
# - enumerate(): Get index + value
# - zip(): Iterate multiple lists together
# - while: Condition-based loops
# - continue: Skip iteration
# - break: Exit loop
# - for-else: Execute else only if no break
# - Walrus operator (:=): Assign + use in one line
# - Dictionary iteration: Loop through dict items
