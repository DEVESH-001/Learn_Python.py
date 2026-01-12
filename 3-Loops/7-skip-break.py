# skip & break : (continue & break)
# Skip -> continue to next iteration
# Break -> exit the loop

flavours = ["Ginger", "Out of stock", "lemon", "discontinue", "Tulsi", "Coco"]

for flavour in flavours:
    if flavour == "Out of stock":
        continue
    if flavour == "discontinue":
        print(f"{flavour} item found")
        break
    print(f"{flavour} item found")

print("Out side of loop")
