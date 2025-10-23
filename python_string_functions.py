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

 
# Join transformation

first_name = "Azharuddin"
last_name = "Khan"

full_name = first_name + " " + last_name
print(full_name)  

folder = "C:/Users/Azharuddin/Documents"
file = "report.pdf"
full_file_path = folder + "/" + file
print(full_file_path)

# f-strings 

name = "Azharuddin"
age = 39
is_student = False

print("My name is " + name + " I am " + str(age) + " years old" + " and my student status  " + str(is_student))

print(f"My name is {name}, i am {age} years old and my student status is {is_student}")

 