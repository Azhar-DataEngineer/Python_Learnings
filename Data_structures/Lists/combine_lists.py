letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
numbers = [1, 2, 3, 4, 5, 6, 7]

combined = letters + numbers
print(combined)
print(letters  * 2)

comb = [letters, numbers]
print(comb)

numbers.extend(letters)
print(letters)
print(numbers)

letters =['a', 'b', 'c']

numbers = [1, 2, 3 , 5]

combined = zip(letters, numbers ,"Hiii")
print(combined)
print(list(combined))


id = [101, 102, 103]

name = ['Alice', 'Bob', 'Charlie']

combined_info = zip(id, name)
print(list(combined_info))
