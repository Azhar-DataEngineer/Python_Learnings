# logical operator
# and operator
print(3 > 1 and 5 < 1)

# or operator
print(3 > 1 or 5 < 1)

cpu_usage = 50  # in percentage
memory_usage = 70  # in percentage

print(cpu_usage > 90 or memory_usage > 90)

# checking credentials befor login

email = True
password = True

print(email and password)

# Logical NOT operator

print(not 3 > 2)

print(not not False)

print(not True)

name = ""

print(not name)  # True because name is an empty string

# control mixed condition

# Default priority to AND operator and then to OR operator

# Use Parentheses to change the priority



is_logged_in = True
is_guest = False
is_banned = True
print((is_logged_in or is_guest) and not is_banned)

# Python Challenge

# check if the user name is not empty or None and age is greater than or equal to 18
username = "azhar"
age = 20

print((username != "" and username is not None) and age >= 18 )


password = "securepas sword123"

print(len(password) >= 8 and not " " in password)

email = "azhar@exampl"

print(email != "" and email is not None and "@" in email and email.endswith(".com"))


# Q4 : Check if a username is a string , is not none an is longer than 5 characters
username = "azhar"


print(isinstance(username , str) and username is not None and len(username) > 5)



user_type = "admin"
is_banned = False
is_email_verified = True

(user_type== 'admin' or user_type == "moderator") and not is_banned and not is_email_verified