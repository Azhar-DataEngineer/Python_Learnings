for x in range(3): #outer loop
    for y in range(2): #inner loop
        for z in range(2): #innermost loop
            print(f"{x}-{y}-{z}")
            


colors = ["Red", "Green", "Blue"]
sizes = ["S", "M", "L"]

for color in colors:
    for size in sizes:
        print(f"Product: {color} - Size: {size}")            
        
        
        
years = [2025, 2026]
months = ["Jan", "Feb", "Mar"]
days = range(1,29)

for year in years:
    for month in months:
        for day in days:
            print(f"reports_{year}_{month}_{day}.csv")
            

table_names = ["users", "orders", "products"]
columns = ["id", "created_date"]

for t in table_names:
    for c in columns:
        print(f"SELECT count(1) FROM {t} where {c} IS NOT NULL;")            