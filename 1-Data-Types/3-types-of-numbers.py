# Numbers : 
          # -> Intergers
            # -> Boolean , Logical_operations
            # -> Real ,float->decimal
                # -> Complex numbers -> 2+3j


# Integer : whole numbers, positive or negative, without decimals, of unlimited length.

black_tea_grams = 14
ginger_grams = 3

total_grams = black_tea_grams + ginger_grams
print(f"Total_grams_of_Base_tea:{total_grams}")

remaining_grams = black_tea_grams - ginger_grams
print(f"Remaining_grams_of_Base_tea:{remaining_grams}")

milk_liters = 7
serving = 4

milk_per_serving = milk_liters / serving
print(f"Milk_per_serving:{milk_per_serving}")


total_tea_bag = 7
pots = 4
# // -> floor division: returns the largest integer less than or equal to the division result
bags_per_pot = total_tea_bag // pots
print(f"Tea_bags_per_pot:{bags_per_pot}")

# % -> modulus: returns the remainder of the division
total_cadamom_pods = 10
pods_per_cup = 3
left_over_pods = total_cadamom_pods % pods_per_cup
print(f"Left_over_cadamom_pods:{left_over_pods}")

# ** -> exponentiation: raises the first number to the power of the second number (2^3 = 8)
base_flavor_strength = 2
scale_factor = 3
powerful_flavor = base_flavor_strength ** scale_factor
print(f"Powerful_flavor_strength:{powerful_flavor}")

# Large Numbers with underscores for better readability
total_tea_leaves_harvested = 1_000_000_000 
print(f"Total_tea_leaves_harvested:{total_tea_leaves_harvested}")