# Types 

name = "Azhar"

# To check the type of variable
print(type(name))

age = 39
print(type(age))
print("Your age is :" + str(age))

age = str(age)
print(type(age))



#  math operations

password = "1234a"

print(len(password))

if len(password) < 8:
    print("Your password is too short")
    
    
text = """
Python is easy to learn.
Python is powerful.
Many people use Python.
"""

print(text.count("Python"))

# Transformation functions
# Replace

price = "1234,56"
print(price.replace(",", "."))

phone = "987-654-3210"

print(phone.replace("-","/"))

print(phone.replace("-",""))


new_price = "$1,299.99"

print(new_price.replace("$","").replace(",",""))


phone_number = "+49 (123) 456-7890"

print(phone_number.replace("+","00").replace(" ","").replace("(","") \
    .replace(")","").replace("-",""))

  
