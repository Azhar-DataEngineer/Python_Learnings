
# Basic Dictionary Operations in Python
info_1 = {'Ron': 25, 'Harry': 30, 'Hermione': 28}
print(info_1)

# Accessing values
info_2 = {'Ron':25, 'Ron':30, 'Hermione':28}
print(info_2['Ron'])

# Using dict() constructor
info_3 = dict(Ron=25, Harry=30, Hermione=28)
print(info_3)

# List of tuples to dictionary
my_list = [('Ron',25), ('Harry',30), ('Hermione',28)]
info_4 = dict(my_list)
print(info_4)

# Tuple of tuples to dictionary
my_tuple = (('Ron',25), ('Harry',30), ('Hermione',28))

print(f"First element of my_tuple: {my_tuple[0]}")

info_5 = dict(my_tuple)
print(info_5)

print(info_5["Harry"])

info_5["Ron"] = 26
# updating existing key

info_5["Azhar"] = 90
# adding new key

print(info_5)
print(f"Mutability demo - updated Ron's age: {info_5}")


#to get all keys in the dictionary
print(info_5.keys())

# to get all values in the dictionary
print(info_5.values())

# to get all key-value pairs in the dictionary
print(info_5.items())

# iterating through dictionary 
for key, value in info_5.items():
    print(f"Key: {key}, Value: {value}")
    
    
info_6 = {'Ron':25, 'Harry':30, 'Hermione':28, 'Ron':35}
info_7 = {'Tom':40, 'Jerry':45 , 'Ron':50}

# Merging two dictionaries
info_8 = {**info_6, **info_7}
print(info_8)

# If there are duplicate keys, the values from the latter dictionary overwrite those from the former
info_9 = {**info_7, **info_6}
print(info_9)

# Length of a dictionary
info_10 = {"Azhar":90, "Debu":85, "Bhaskar":95}

print(len(info_10))


del info_10["Debu"]

print(info_10)

info_11 ={"Delhi" : "India", "Tokyo": "Japan", "Canberra": "Australia"}

del info_11

# print(info_11)

info_12 = {"Kohli" : "India", "Smith": "Australia", "Root": "England"}

# Clearing all items from the dictionary 
info_12.clear()

print(info_12)
# Data Engineering Use Case: Schema Mapping and Transformation

info_13 = {"Mumbai Indians": "MI", "Chennai Super Kings": "CSK", "Royal Challengers Bangalore": "RCB"}  

# Pop an item with key "Chennai Super Kings" it returns the value associated with the key being removed
print(info_13.pop("Chennai Super Kings"))

print(info_13)


info_14 = {"Sachin":100, "Dravid":80, "Laxman":90}

# Check if key exists
"Sachin" in info_14  # returns True
print("Sachin" in info_14)

print("Ganguly" in info_14)  # returns False

info_15 = {"A":1, "B":2, "C":3}
info_16 = {"A":1, "B":2, "C":3}

print(info_15 == info_16)  # True as both have same key-value pairs

print(info_15 != info_16)  # False as both have same key-value pairs

# Example 1: API Response Parsing
# api_response = {
#     "user_id": 12345,
#     "user_name": "John Doe",
#     "email": "john@example.com",
#     "created_timestamp": "2024-01-15T10:30:00Z"
# }

# # Transform to internal schema
# transformed_data = {
#     "id": api_response["user_id"],
#     "name": api_response["user_name"],
#     "contact": api_response["email"]
# }
# print(f"API to Internal Schema: {transformed_data}")


# Example 2: ETL Configuration
# etl_config = {
#     "source_db": "postgres",
#     "target_db": "snowflake",
#     "batch_size": 1000,
#     "retry_attempts": 3
# }

# for config_key, config_value in etl_config.items():
#     print(f"Config {config_key}: {config_value}")


# # Example 3: Data Quality Checks
# data_quality_rules = {
#     "customer_id": {"check": "not_null", "threshold": 100},
#     "order_amount": {"check": "positive", "threshold": 0},
#     "email": {"check": "format", "threshold": "regex"}
# }

# for column, rule in data_quality_rules.items():
#     print(f"Column: {column} -> Check: {rule['check']}, Threshold: {rule['threshold']}")


# # Example 4: Partition Configuration
# partition_config = {
#     "sales_data": {"partition_by": "order_date", "partition_type": "daily"},
#     "user_events": {"partition_by": "event_timestamp", "partition_type": "hourly"}
# }

# for table, config in partition_config.items():
#     print(f"Table: {table}, Partition By: {config['partition_by']}, Type: {config['partition_type']}")

# Source column to target column mapping plus metadata
# column_map = {
#     "cust_id": {"target": "customer_id", "type": "NUMBER", "nullable": False},
#     "cust_name": {"target": "customer_name", "type": "STRING", "nullable": True},
#     "signup_ts": {"target": "created_at", "type": "TIMESTAMP_NTZ", "nullable": False},
# }

# for source_col, details in column_map.items():
#     print(f"Source Column: {source_col} as Target Column: {details['target']}, Type: {details['type']}, Nullable: {details['nullable']}")
    
    
    
info_17 = {'A':1, 'B':2, 'C':3}

info_18 = info_17.copy()

print(info_18)

info_19 = {"A":10, "B":20, "C":["Freddy", "John", "Smith"]}

info_20 = info_19.copy()

print(info_19)  
print(info_20)

info_20["C"][2]="Sachin"

print(info_20)

print(info_19)

msg = {'A': 'Sleep', 'B': 'Eat', 'C': ['Play','Study','Code']}

import copy

information = copy.deepcopy(msg)

print(msg)
print(information)


square = {x: x*x for x in range(0,3)}

print(square)
    