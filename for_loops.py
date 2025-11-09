print("Round 1")
print("Round 2")
print("Round 3")
print("Round 4")
print("Round 5")


items = [1, 2, 3, 4, 5,"Hi", "Hello"]

# Try to keep the naming convention meaningful
for item in items:
    print(f"Round {item}")
    
# Sequence - List , Tuple , String , Range function, Dict are sequences
items = " Python"


for item in items:
    print(f"Character : {item}")
    
for number in range(1, 11):
    print(f"Number : {number}")
  
#  With only stop parameter
for number in range(5):
    print(f"Number : {number}")
    
# With bnoth start and stop parameter
for number in range(1, 5):
    print(f"Numbering : {number}")
    
# With start , stop and step parameter 
for number in range(1, 10, 2):
    print(f"Odd Numbers : {number}")
    
for number in range(2, 10, 2):
    print(f"Even Numbers : {number}")

# Why do we need loops in business use case?

scores = [80, 90, 75, 88, 92]
total_score = 0

for score in scores:
    total_score += score
    print(f"Current Total Score: {total_score}")
    
print(f"Final Total Score: {total_score}")
    
    
files = ["File1.csv", " file2.csv", "file3.txt"]

for file in files:
    file = file.strip().lower().replace(".txt", ".csv")
    print(f"Processing file: {file}")
    
# 