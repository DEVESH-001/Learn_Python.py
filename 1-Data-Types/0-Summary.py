# Collections : are data structures that can hold multiple items.

# Types of Collections in Python:
# 1. List : An ordered collection of items which can be of different data types.
# Lists are defined using square brackets [] and items are separated by commas.
# how it works: Lists maintain the order of elements and allow duplicate values.    
fruits = ["apple", "banana", "cherry", "date", "apple"]
print("Initial Fruits List:", fruits)


# 2. Tuple : An ordered collection of items which can be of different data types.
# Tuples are defined using parentheses () and items are separated by commas.
# how it works: Tuples maintain the order of elements and allow duplicate values. Tuples are immutable (cannot be changed after creation).
vegetables = ("carrot", "broccoli", "spinach", "kale", "carrot")
print("Initial Vegetables Tuple:", vegetables)

# 3. Set : An unordered collection of unique items.
# Sets are defined using curly braces {} with items separated by commas.
# how it works: Sets automatically remove duplicate values and do not maintain any specific order of elements.
essential_spices={"salt", "pepper", "cumin", "ginger", "paprika"}
optional_spices={"oregano", "basil", "ginger", "cumin", "paprika"}  
all_spices = essential_spices.union(optional_spices)
print("All Spices:", all_spices)

# 4. Dictionary : A dictionary is a collection of key-value pairs. Each key is unique and is used to store and retrieve values.
# Dictionaries are defined using curly braces {} with key-value pairs separated by colons (:).
# how it works: You can access, add, remove, and modify values in a dictionary using their corresponding keys.

# 5. Frozen Set : An immutable version of a set. Once created, the elements of a frozen set cannot be changed.
# Frozen sets are defined using the frozenset() function.
# how it works: Frozen sets maintain unique elements but do not allow any modifications after creation.
immutable_spices = frozenset(["turmeric", "coriander", "cloves", "nutmeg"])
print("Immutable Spices (Frozen Set):", immutable_spices)

# 6. Bytearray : A mutable sequence of bytes.
# Bytearrays are defined using the bytearray() function.
# how it works: Bytearrays allow modification of individual bytes and support various byte-level operations.

