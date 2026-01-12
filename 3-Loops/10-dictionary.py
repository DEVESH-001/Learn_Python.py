users =[
    {"id": 1, "total": 100, "coupon": "P20"},
    {"id": 2, "total": 200, "coupon": "X15"},
    {"id": 3, "total": 300, "coupon": "F50" },
]

# Dictionary of discounts
discounts={
    "P20": (0.2,0), # 20% discount
    "X15": (0.5,0), # this is tuple (percentage, fixed amount)
    "F50": (0.8,0)
}

for u in users:
    percent, fixed = discounts.get(u["coupon"], (0,0))
    discount = u["total"] * percent + fixed
    print(f"{u['id']} paid {u['total'] - discount} Discount: {discount}")