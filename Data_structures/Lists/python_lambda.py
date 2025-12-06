multiply = lambda x: x * 2

print(multiply(5))


addition=lambda x,y: x + y
print(addition(3,7))

check = lambda i: i in "Python"

print(check("z"))

# Lambda with Map


prices = ["$12.50", "$9.99", "$5.75", "$20.00"]

p = "$12.50"
print(type(float(p.replace("$",""))))

print(list(map(lambda p: float(p.replace("$","")), prices)))

# Lambda with Filter

prices = [120, 99, 75, 200, 150, 50, 300]

print(list(filter(lambda p: p >=100 , prices)))

students = [['Azhar',85],
            ['Bina',92],
            ['Cathy',78],
            ['David',90],
            ['Eva',88]
           ]

print(students[0][1] > 80)

print(filter(lambda row: row[1] > 80, students))
print(list(filter(lambda row: row[1] > 80, students)))
           
student = [['Azhar',85],
           ['Anjana',90],
           ['Bina',78],
           ['Cathy',92]]

print(student[2][0].startswith("A"))

filter(lambda row: row[0].startswith("A"), student)
print(list(filter(lambda row: row[0].startswith("A"), student)))

# Example: Using lambda with sorted (iterable)
# Suppose you have a list of tuples and want to sort by the second element
items = [('apple', 3), ('banana', 1), ('cherry', 2)]

# sorted() returns a new sorted list, does not change the original
sorted_items = sorted(items, key=lambda x: x[1])
print(sorted_items)  # Output: [('banana', 1), ('cherry', 2), ('apple', 3)]

# ---
# Layman Explanation:
# - 'lambda x: x[1]' is a quick way to tell Python to use the second value in each tuple for sorting.
# - 'sorted' creates a new list, leaving the original unchanged.
# - Imagine sorting a list of (fruit, quantity) by quantity, not by name.
# ---