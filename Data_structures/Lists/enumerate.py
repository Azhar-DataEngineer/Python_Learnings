letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

reversed_letters = reversed(letters)

enumerate_letters = enumerate(letters)

# print(list(enum       erate_letters)) 

for l in reversed_letters:
    print(l)


for index, value in enumerate(letters):
    print(f"Index: {index}, Value: {value}")   
    
    
    
numbers = [10, 20, 30, 40, 50] 

print(zip(letters, numbers))

print(list(zip(letters, numbers)))

for i, v in zip(letters, numbers):
    print(f"Letter: {i}, Number: {v}")

