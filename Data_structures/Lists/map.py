letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

print(map(str.upper, letters))

print(list(map(str.upper, letters)))


numbers = ['10', '20', '30', '40', '50']

print(list(map(int, numbers)))


names = [' alice ', '  bob', 'charlie  ']

map(str.strip, names)

print(list(map(str.strip, names)))

for m in map(str.strip, names):
    print(f"'{m}'")