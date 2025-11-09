items  = [1,3,5,7]

for item in items:
    if item%2==0:
        print(f"Even number found: {item}")
        break
else:
    print("All numbers are odd.")
    
    
    
# list of names
# names = ["Alice", "Bob",None, "`Charlie"]

names = ["Alice", "Bob","Charlie"]
for name in names:
    if name is None:
        print("Invalid name found, stopping the loop.")
        break
else:
    print("All names are valid.")
    
# Example of forelse with break 
files = ["data1.csv", "data2.csv","abc.pdf", "pqr.png", "data3.csv"]

for file in files:
    if not file.endswith(".csv"):
        print(f"Not a CSV file found: {file}")
        break    
else:
    print("All files are CSV files.")
    
# Example of forelse with continue
    
# files = ["data1.csv", "data2.csv", "image.png"]
files = ["data1.csv", "data2.csv","abc.pdf", "pqr.png", "data3.csv"]

for file in files:
    if not file.endswith(".csv"):
        print(f"Not a CSV file found: {file}")
        continue    
else:
    print("All files are CSV files.")
    
    
    # doesn't make sense to have else with continue only with break
    
file_list = ['report1.pdf', 'report2.pdf', 'summary.docx', 'data.csv','report1.pdf']
file_processed = []

for file in file_list:
    print(f"Processing file: {file}")
    if file in file_processed:
        print(f"Duplicate file found: {file}, stopping processing.")
        break
    file_processed.append(file)
    print(file_processed)
    
else:
    print("All files are unique")   