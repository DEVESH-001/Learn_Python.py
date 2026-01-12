# for-else : The else block after a for loop executes only if the loop completes normally without encountering a break statement.
# Syntax:
# for item in iterable:
#     # code block to be executed
# else:
#     # code block to be executed if loop completes normally

staff = [("Devesh", 24), ("Ankita", 22), ("Ravi", 28), ("Sneha", 26)]

for name, age in staff:
    if age <= 30:
        print(f"{name} ")
        break
else:
    print("No one is eligible")
