
# Memebership Operators in Python
print("o" in "hello")  # Check membership in string

print(3 not in [1, 2, 3, 4, 5])  # Check membership in list

domain = "gmail.com"

banned_domains = {"spam.com", "banned.com", "fake.com"}

print(domain in banned_domains)  # Check membership in set

# Identity Operators in Python


a = [1,2,3]
b = [1,2,3]

print(a == b)  # True because values are the same
print(a is b)  # False because they are different objects in memory

x = 5
y =5

print(x == y)  # True because values are the same
print(x is y)  # True because small integers are cached in Python



x = [1,2,3]
y = x

print(x == y)  # True because values are the same
print(x is y)  # True because both refer to the same object in memory

# Make sure the email exists and it is not empty
email = ""

print(email != "" and email is not None)
