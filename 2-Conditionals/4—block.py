# pass : This is a placeholder statement in Python.(it ignores the block of code)
# It is used when a statement is syntactically required but no action is needed.


device_status = "active"
temperatue = 38

if device_status == "active":
    if temperatue > 35:
        print("High Temp!!!")
    else:
        print("Temp is Normal :)")
else:
    print("Device is offline")
