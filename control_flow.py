print(True)
print(False)

print(type(True))

print(bool(1))

print(bool(1.0))

print(bool())

print(bool(0))

print(bool(""))


print(bool(None))

email = "abc@gmail.com"
phone = "1234567890"
username = "azhar" 

# Allow registration if at least one contact method is provided

print(any([email, phone, username]))  # Output: True


print(all([email, phone, username]))

print(isinstance(True, bool))  # Check if True is an instance of bool