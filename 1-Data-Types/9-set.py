# Sets: are unordered collections of unique elements, defined by curly braces {}
# how it works: Sets automatically remove duplicate values and do not maintain any specific order of elements.

essential_spices={"salt", "pepper", "cumin", "ginger", "paprika"}
optional_spices={"oregano", "basil", "ginger", "cumin", "paprika"}

all_spices = essential_spices.union(optional_spices)
print("All Spices:", all_spices)

common_spices =essential_spices & optional_spices
print("Common Spices:", common_spices)

# difference
unique_essential_spices = essential_spices - optional_spices # spices in essential_spices but not in optional_spices
print("Unique Essential Spices:", unique_essential_spices)

print(f"Is 'salt' an essential spice? {'salt' in essential_spices}")