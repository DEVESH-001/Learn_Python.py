# elif: it stands for "else if", it allows you to check multiple conditions in sequence.

# a program to calculate the price based on size
# task : input "small","medium","large"
# small—>$10, medium—>$15, $20

cup_size = input("Choose your cup size [small/medium/large]: ").lower()

if cup_size == "small":
    print("Price —> $10")
elif cup_size == "medium":
    print("Price —> $15")
elif cup_size == "large":
    print("Price —> $20")
else:
    print("Come back later")
