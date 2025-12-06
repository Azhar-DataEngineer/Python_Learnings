letters = ['a',1,'b','c',None, '', False]

filter(None, letters)

print(list(filter(None, letters)))

print(list(filter(bool, letters)))

languages = ['Python', 'Java', 'C', 'JavaScript', 'Ruby', 'Go', 'C++','12'] 

filter(str.isalpha, languages)

print(list(filter(str.isalpha, languages)))

for i in filter(str.isalpha, languages):
    print(i)

