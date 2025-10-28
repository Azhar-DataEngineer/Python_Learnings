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

print(f"2+3 = {2+3}")
#  25.00

stamp = "2025-10-25"

print(stamp.split("-"))

csv_data = "Azhar,Data Engineer,39,India"

csv_data_list = csv_data.split(",")
print(csv_data_list)

# String Repeatition
print("ha" * 5)

# extraction via indexing 

text = "Python" 

# Extracting the first character

print(text[0])
print(text[-6])  # Negative indexing to get the first character

#  Extracting the last character

print(text[5])
print(text[-1])  # Negative indexing to get the last character

# Extracting the character "h" from "Python" string
print(text[3])
print(text[-3])  # Negative indexing to get the fourth character


# Indexes and Slicing

date = "2025-10-28"

print(date[0:4])  # Extracting the year

print(date[:4])  # Extracting the year

print(date[5:7])  # Extracting the month

print(date[8:])  # Extracting the day
print(date[-2:])  # Extracting the day using negative indexing

# how to clean white spaces

text = " Engineering"
print(text)
text.lstrip()  # Remove leading white spaces
print(text.lstrip())


text = "Data  "
print(text)
text = text.rstrip()  # Remove trailing white spaces
print(text)

text = "                   Science  "
print(text)
text = text.strip()  # Remove leading and trailing white spaces
print(text)

text ="Data Engineering"
print(text.strip())

text = "###ABC###"
text = text.strip("#")
print(text)


text = "   Engineering" 

# print(len(text))
# text = text.strip()  # Remove leading white spaces
# print(len(text))

no_of_spaces = len(text) - len(text.strip())
print("No of spaces: ",no_of_spaces)

# Case Conversion

text = "python PROGRAMMING" 

print(text.lower())
print(text.upper())

search = "Email "
data = "email"

print(search.lower().strip() == data.lower().strip())

# Advance challenge

text = "968-Maria,(  D@t@ Engineer );; 27y  "

print("name: " + text[4:9].lower() + " | " + "role: " + text[13:27].lower().replace("@","a") + " | " + "age: " + text[-5:-3].strip())

# Search String Functions

phone = "+91 987-654-3210"

print(phone.startswith("+92"))

email = "baraa@gmail.com"

print(email.endswith("gmail.com"))

file = "data_report.pdf"

print(file.endswith(".pdf"))

print("@" in email)


url = "https://api.example.com/v12/resources"

print("/api" in url)

phone1 = "+1-123-456-7890"
phone2 = "48-987-654-3210"
phone3 = "00048-987-654-3210"



print(phone1[3:])
print(phone1[phone1.find("-")+1:])

print(phone2[3:])
print(phone2[phone2.find("-")+1:])
print(phone3[6:])
print(phone3[phone3.find("-")+1:])

# validation functions
country = "India123" 

print(country.isalpha())  # Check if all characters are alphabetic

phone = "01233-4567890"

# phone.is_numeric()  # Check if all characters are numeric
print(phone.isnumeric())