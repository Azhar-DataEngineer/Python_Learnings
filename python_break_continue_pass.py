# break statement example

names = ["Alice", "Bob", "", "David"]

for name in names:
    if name == "":
        print("Empty name found, stopping the loop.")
        break
    print(f"Name: {name}")


for name in names:
    if name == "":
        print("Empty name found, stopping the loop.")
        continue
    print(f"Name: {name}")    
    
for name in names:
    if name == "":
        # print("Empty name found, stopping the loop.")
        pass #todo Handle empty name case later
        name = name.replace("", "Unknown")
    print(f"Name: {name}")        
    
print("-----")

# Skipping weekends in calendar loop - we will use continue 

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
weekends = ["Saturday", "Sunday"]
for day in days:
    if day in weekends:
        continue
    print(f"Working day: {day}")
    
    
    # 
    
emails = [
 'data@gmail.com',
 'azhar@outlook.com',
 'DROP TABLE users;',
 'dev@gmail.com'
]
    
    
for email in emails:
    if ";" in email:
        print("Potentially malicious email found, skipping.")
        break
    print(f'Processing email: {email}')

