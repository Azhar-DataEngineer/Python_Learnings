letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']


letters_copy = letters 

letters.pop()
letters_copy.append('A')

print("Original list:", letters)
print("Copied list:", letters_copy)


letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

copy_letters = letters.copy()

copy_letters.append('Z')

print("Original list before modification:", letters)
print("Copied list before modification:", copy_letters)

# deep Copy

matrix = [ ['a' ,'b','c' ],
              ['d','e','f']]

matrix_copy = matrix.copy()

matrix.pop()

print("Original matrix before modification:", matrix)
print("Copied matrix before modification:", matrix_copy)

print("------Deep Copy Example------")
import copy

matrix = [ ['a' ,'b','c' ],
              ['d','e','f']]

matrix_deepcopy = copy.deepcopy(matrix)

print("Original matrix before modification:", matrix)
print("Deep Copied matrix before modification:", matrix_deepcopy)

matrix.pop()


print("Original matrix after modification:", matrix)
print("Deep Copied matrix after original modification:", matrix_deepcopy)

matrix_deepcopy[0].append('Z')
print("Original matrix after deep copied modification:", matrix)
print("Deep Copied matrix after its own modification:", matrix_deepcopy)


print("------End of Shallow Copy Example------")

matrix = [ ['a' ,'b','c' ],
              ['d','e','f']]

matrix_shallowcopy = copy.copy(matrix)

print("Original matrix before modification:", matrix)
print("Shallow Copied matrix before modification:", matrix_shallowcopy)

matrix.pop()

print("Original matrix after modification:", matrix)
print("Shallow Copied matrix after original modification:", matrix_shallowcopy)

matrix_shallowcopy[0].append('Z')
print("Original matrix after shallow copied modification:", matrix) 
print("Shallow Copied matrix after its own modification:", matrix_shallowcopy)


import copy

original_list = [ 
                 ['a','b'], # row1
                 ['c','d']  # row2
                ]

copy1 = original_list          # Reference Copy
print(original_list is copy1)  # True
print(original_list[0] is copy1[0])  # True
print(original_list[0][0] is copy1[0][0])  # True

# Shallow Copy
copy2 = original_list.copy()
print(original_list is copy2)  # False
print(original_list[0] is copy2[0])  # True
print(original_list[0][0] is copy2[0][0])  # True

copy3 = copy.deepcopy(original_list)  # Deep Copy
print(original_list is copy3)  # False
print(original_list[0] is copy3[0])  # False
print(original_list[0][0] is copy3[0][0])  # False