# match: match is used to compare a value against multiple cases, similar to switch-case in other languages.

seat_type = input("Enter seat type (sleeper/AC/general/luxury) : ").lower()

# Using match-case statement to handle different seat types
match seat_type:
    case "sleeper":
        print("Sleeper — No AC, bed ✅")
    case "ac":
        print("AC — Air Conditioned, Comfort 😌")
    case "general":
        print("General — Cheapest, Comfort ❌")
    case "luxury":
        print("Luxury — Best In Class ⭐️")
    case _:
        print("INVALID !!!")
