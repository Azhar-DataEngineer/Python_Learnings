# Ternary Operator or Inline If-Else Statement in Python
# Use only if you have a simple if-else condition


score = 100 
if score >=90:
    print("A")
elif score >= 80:
    print("B")
else:
    print("C")

# Using Ternary Operator
score = 20
grade = "A" if score >= 90 else "B" if score >= 80 else "C"
print(grade)

# Special Statment match cases

country = "Pakistan"

if country == "India":
    print("IND")
elif country == "United States":
    print("USA")
elif country == "United Kingdom":
    print("UK")    
else:
    print("Unknown Country")
    
    # Only in Python 3.10 and above
match country:
    case "India":
        print("IND")
    case "United States":
        print("USA")
    case "United Kingdom":
        print("UK")
    case _:
        print("Unknown Country")    