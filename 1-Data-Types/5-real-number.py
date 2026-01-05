import sys
ideal_temp = 93.2
current_temp = 95.5999999999
from  fractions import Fraction

print(f"Ideal_temp:{ideal_temp}")
print(f"Current_temp:{current_temp}")
print(f"difference-in-temp:{current_temp - ideal_temp}")


print(sys.float_info)

# Using Fraction for precise decimal representation
ideal_temp_fraction = Fraction(932, 10)