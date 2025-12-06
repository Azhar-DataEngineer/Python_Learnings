a = {10,20,30,40}

b = {30,40,50,60}

# Mathematical Operations

print(a.union(b))
# Union of two sets
print(a | b)
# Union using | operator

# intersetion 
print(a.intersection(b))
# Intersection of two sets
print(a & b)
# Intersection using & operator

#Difference
print(a.difference(b))
# Difference of two sets (a - b)

print(a - b)
# Difference using - operator


print(b.difference(a))
# Difference of two sets (b - a)

print(b - a)
# Difference using - operator

# Symmetric Difference
print(a.symmetric_difference(b))

# Symmetric Difference of two sets
print(a ^ b)
# Symmetric Difference using ^ operator