# Creating a list of letters to demonstrate list operations
# Lists in Python are ordered collections that can be modified (mutable)
letters = ['a', 'b', 'c', 'd', 'e']
print("Original list:", letters)
letters.append('f')  # Adds 'f' to the end of the list
letters.append('g')  # Adds 'g' to the end of the list
print("After append:", letters)
# ---
# Example: Adding items to a list (append)
# Input: ['a', 'b', 'c', 'd', 'e']
# Output: ['a', 'b', 'c', 'd', 'e', 'f', 'g']
# Explanation: 'append' adds new items to the end of the list, like adding new books to the end of a shelf.
# ---

letters.insert(0, 'A')
print("After insert at index 0:", letters)  # Inserts 'A' at the beginning (index 0)
# ---
# Example: Inserting an item at a specific position
# Input: ['a', 'b', 'c', 'd', 'e', 'f', 'g']
# Output: ['A', 'a', 'b', 'c', 'd', 'e', 'f', 'g']
# Explanation: 'insert' places an item at the position you choose, like putting a new book at the start of a shelf.
# ---

matrix = [ ['a' ,'b','c' ],
              ['d','e','f'],
              ['g','h','i'] ]
print("Original matrix:", matrix)
# ---
# Example: 2D lists (matrices) for organizing data in rows and columns
# Input: [['a','b','c'], ['d','e','f'], ['g','h','i']]
# Output: Same as input
# Explanation: Think of this as a table or spreadsheet, where each row is a list inside a bigger list.
# ---

matrix.append(['x','y','z'])
print("After append:", matrix)
# ---
# Example: Adding a new row to a matrix
# Input: matrix before append
# Output: matrix with new row ['x','y','z'] added at the end
# Explanation: Like adding a new row to a table.
# ---

matrix = [ ['a' ,'b','c' ],
              ['d','e','f'],
              ['g','h','i'] ]
print("Original matrix:", matrix)

matrix.insert(0 ,['p','q','r'])
print("After insert at index 0:", matrix)
# ---
# Example: Inserting a new row at the top of a matrix
# Input: matrix before insert
# Output: matrix with new row ['p','q','r'] at the top
# Explanation: Like adding a header row to a table.
# ---

matrix = [ ['a' ,'b','c' ],
              ['d','e','f'],
              ['g','h','i'] ]
print("Original matrix:", matrix)

matrix[1].append('x')
print("After appending 'x' to the second row:", matrix)
# ---
# Example: Adding an item to a specific row in a matrix
# Input: matrix before append
# Output: matrix with 'x' added to second row
# Explanation: Like adding a new column value to a specific row in a table.
# ---

matrix[0].insert(0,'z')
print("After inserting 'z' at the beginning of the first row:", matrix)
# ---
# Example: Inserting an item at the start of a row
# Input: matrix before insert
# Output: matrix with 'z' at the start of first row
# Explanation: Like adding a new column at the start of a table row.
# ---

# Removing evertyhign from the list
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print("Original list:", letters)
letters.clear()
print("After clear:", letters)
# ---
# Example: Clearing all items from a list
# Input: ['a', 'b', 'c', 'd', 'e', 'f', 'g']
# Output: []
# Explanation: 'clear' removes everything, like emptying a shelf.
# ---

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print("Original list:", letters)
letters.remove('c')  # Removes the first occurrence of 'c'
print("After remove 'c':", letters)
# ---
# Example: Removing a specific item from a list
# Input: ['a', 'b', 'c', 'd', 'e', 'f', 'g']
# Output: ['a', 'b', 'd', 'e', 'f', 'g']
# Explanation: 'remove' deletes the first matching item, like removing a book by title.
# ---

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print("Original list:", letters)
letters.pop(0)
print("After pop at index 0:", letters)
removed_letter=letters.pop(-1)
print(f"Removed letter: {removed_letter}")
# ---
# Example: Removing items by position (pop)
# Input: ['a', 'b', 'c', 'd', 'e', 'f', 'g']
# Output: After pop(0): ['b', 'c', 'd', 'e', 'f', 'g']
# Output: After pop(-1): ['b', 'c', 'd', 'e', 'f'] and removed_letter = 'g'
# Explanation: 'pop' removes an item at a specific position, like taking a book from a certain spot.
# ---

matrix = [ ['a' ,'b','c' ],
              ['d','e','f'],
              ['g','h','i'] ]
print("Original matrix:", matrix)
matrix.remove(['a' ,'b','c' ])
print("After removing first row:", matrix)
matrix.pop()
print("After popping last row:", matrix)
# ---
# Example: Removing rows from a matrix
# Input: matrix before remove/pop
# Output: matrix with first row removed, then last row removed
# Explanation: Like deleting rows from a table.
# ---

matrix = [ ['a' ,'b','c' ],
              ['d','e','f'],
              ['g','h','i'] ]
print("Original matrix:", matrix)
matrix[1].remove('e')
print("After removing 'e' from second row:", matrix)
matrix[-1].pop(0)
print("After popping first element from last row:", matrix)
matrix[0].pop(-1)
print("After popping last element from first row:", matrix)
# ---
# Example: Removing items from specific rows in a matrix
# Input: matrix before remove/pop
# Output: matrix with items removed from specific rows
# Explanation: Like erasing a cell in a spreadsheet.
# ---

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print("Original list:", letters)
letters[0] = 'A'
print("After updating index 0 to 'A':", letters)
# ---
# Example: Updating an item in a list
# Input: ['a', 'b', 'c', 'd', 'e', 'f', 'g']
# Output: ['A', 'b', 'c', 'd', 'e', 'f', 'g']
# Explanation: Assigning a new value to a position, like replacing a book on a shelf.
# ---

matrix = [ ['a' ,'b','c' ],
              ['d','e','f'],
              ['g','h','i'] ]
print("Original matrix:", matrix)
matrix[-1] = ['x','y','z']
print("After updating last row:", matrix)
matrix[0][0] = 'P'
print("After updating first element of first row to 'P':", matrix)
matrix[1][2] = 'Q'
print("After updating third element of second row to 'Q':", matrix)
matrix[-1][1] = 'R'
print("After updating second element of last row to 'R':", matrix)
# ---
# Example: Updating rows and items in a matrix
# Input: matrix before updates
# Output: matrix with updated rows/items
# Explanation: Like editing values in a table or spreadsheet.
# ---