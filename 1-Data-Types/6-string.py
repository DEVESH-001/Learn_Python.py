#Strings: are used to represent text data in Python & they are immutable
# string -> core, indexing , slicing, concatenation, repetition

chai_type = "ginger chai" # String literal enclosed in double quotes

customer_name = "devesh"

print(f"Order for {customer_name}: {chai_type}")


chai_description = 'A warm and spicy beverage made with black tea, milk, and a blend of aromatic spices like ginger, cardamom, and cinnamon.'


print(f"Description: {chai_description[0:7]}") # Slicing: Extracting substring "A warm"
print(f"Description: {chai_description[0:7:2]}") # Slicing with step: Extracting every 2nd character from "A warm ", 
print(f"Description: {chai_description[::-1]}") # Reversing the string using slicing


label_text = "Chai Lattê" # Unicode string with special character 'ê'
ecoded_lable = label_text.encode('utf-8') # Encoding to UTF-8 bytes
print(f"NON-Encoded Label: {label_text}")
print(f"Encoded Label: {ecoded_lable}")

#proper way to decode
decoded_label = ecoded_lable.decode('utf-8') # Decoding back to string
print(f"Decoded Label: {decoded_label}")