person = ['Maria',29,'Data Scientist','New York']
"""
Demonstrates Python sequence unpacking techniques with lists.
This module shows different ways to extract values from a list:
1. Traditional index-based access (commented out)
2. Basic unpacking - assigns each list element to individual variables
3. Extended unpacking with *args - captures multiple elements into a single variable
4. Partial unpacking - extracts specific elements while grouping the rest
The person list contains: [name, age, profession, location]
Examples:
- Basic unpacking: name, age, profession, location = person
- Star unpacking: name, *details, country = person (details gets middle elements)
- Remaining capture: name, *details = person (details gets all remaining elements)
This demonstrates Python's powerful unpacking syntax for cleaner, more readable code
compared to manual indexing.
"""
# Basic unpacking: assigns each list element to corresponding variables
# Extended unpacking: captures name and location separately, groups middle elements
# Partial unpacking: gets first element, captures all remaining in details list

# name = person[0]
# age = person[1]
# profession = person[2]      
# location = person[3]

# smarter way via unpacking
name, age, profession, location = person
print(name)
print(age)      
print(profession)
print(location)

name , *details , country = person

print(name)

print(details)

print(country)


name , *details = person
print(name)
print(details)


name, _ , role, _ = person
print(name) 
print(role)

# List of all random numbers in the list except first and last
numbers = [10, 23, 45, 67, 89, 12, 34]

first,*_,last = numbers

print(first)
print(last)


