a = {10,20,30,40}

a.add(50)
print(a)
# unordered when printed after addition 

a.add(20)
print(a)
# no duplicates - unique items only even after addition

a.update("Hi")
print(a)
# adds each character as separate item in case of string

a.update([60,70,80])
print(a)
# adds each item from the iterable

a.update({90,100,110,20})
print(a)
# adds each item from the iterable set but ignores duplicate 20


a |= {120,130}
print(a)
# union operator to add items from another set using |=

a.remove(10)
print(a)
# removes the specified item, raises KeyError if item not found

# a.remove(999)
# raises KeyError as 999 not found in the set

a.discard(999)
print(a)
# removes the specified item, does not raise error if item not found

a.pop()
print(a)
# removes and returns an arbitrary item from the set - Not recommended for specific item removal




