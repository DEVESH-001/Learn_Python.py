def add_vat(price,vat_rate):
    return price * (100 +vat_rate)/100

orders = [100, 20]

for price in orders:
    final_amount = add_vat(price, 15)
    print(f"Original Price: ${price}")
    print(f"Price after VAT: ${final_amount}")
