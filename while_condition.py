# classical while loop

count = 1 #Iniitialization

while count <= 5: # Condition
    print(count)
    count += 1 # Increment/Decrement/Update
    
    

answer = ""

while answer != "yes":
    answer = input("Do you want to exit? (yes/no): ").lower()
    print(f"You entered: {answer}")
    
print("Exited the loop.")