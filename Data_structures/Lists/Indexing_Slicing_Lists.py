# Access & Read
lst = ['a', 'b', 'c', 'd', 'e']

print(lst)

# access only one item via indexing

print(lst[0])  # first item

print(lst[2])  # third item

print(lst[-1]) # last item


matrix = [['a','b','c'],
          ['d','e','f'],
            ['g','h','i']]


print(matrix)

print(matrix[-1]) # access third row

print(matrix[-1][-1]) # access last item in third row


# Slicing

lst = ['a', 'b', 'c', 'd', 'e']

lst[:2] # first 2 items

print(lst[:2])

print(lst[3:])

print(lst[:])

print(matrix[:2])

print(matrix[1:])

print(matrix[-1][:2])