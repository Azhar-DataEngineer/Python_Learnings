# standalone if

score = 60
submitted_project = False

if score >= 90 and submitted_project:
    print("A+")
elif score >= 90:
    print("A")
elif score >= 80:    
    print("B")
elif score >= 70:
    print("C")
elif score >= 60 or submitted_project:
    print("D")
else:
    print("F")
    
# Connecting conditions with logical operators
    
# Independent If else


score = 60
submitted_project = False

if score >= 90:
    print("High Score")
else:
    print("Low Score")
    
if submitted_project:
    print("Project Submitted")
else:
    print("Project Not Submitted")  
    
# Q1: Validate the Quality and Correctness of Email Values

email="abc@gmail.com%%"

# email !="" and "@" in email and "." in email and (email.endswith(".com") or email.endswith(".org") or 
# email.endswith(".net")) and len(email) <= 254 and (email.startswith)

email = email.strip()

if email == "":
    print("Email cannot be empty.")
elif not ("." in email and "@" in email):
    print("Email must contain '.' and '@' characters.")
elif email.count("@") != 1:
    print("Email must contain exactly one '@' character.")
elif not (email.endswith(".com") or email.endswith(".org") or email.endswith(".net")):
    print("Email must end with .com, .org, or .net.")
elif len(email) > 254:
    print("Email length must not exceed 254 characters.")
elif not(email[0].isalnum() and  email[-1].isalnum()):
    print("Email must start and end with a letter or digit")
else:
    print("Email is valid.")
    
    
if email == "":
    print("Email cannot be empty.")
if not ("." in email and "@" in email):
    print("Email must contain '.' and '@' characters.")
if email.count("@") != 1:
    print("Email must contain exactly one '@' character.")
if not (email.endswith(".com") or email.endswith(".org") or email.endswith(".net")):
    print("Email must end with .com, .org, or .net.")
if len(email) > 254:
    print("Email length must not exceed 254 characters.")
if not(email[0].isalnum() and  email[-1].isalnum()):
    print("Email must start and end with a letter or digit")
else:
    print("Email is valid.")    

print("\n" + "="*60)
print("🏔️ SQL SERVER TO SNOWFLAKE CONVERSION")
print("="*60)

# Original SQL Server syntax:
print("📊 ORIGINAL SQL SERVER SYNTAX:")
sql_server_query = "SUBSTRING(TaskSubject,0,CHARINDEX('_',TaskSubject))=CherwellTicketID"
print(f"   {sql_server_query}")

print("\n❄️ CONVERTED SNOWFLAKE SYNTAX:")
snowflake_query = "SUBSTRING(TaskSubject, 1, POSITION('_', TaskSubject) - 1) = CherwellTicketID"
print(f"   {snowflake_query}")

print("\n🔄 KEY DIFFERENCES EXPLAINED:")
print("-" * 40)
print("1. SUBSTRING indexing:")
print("   SQL Server: SUBSTRING(string, 0, length)    # 0-based")
print("   Snowflake:  SUBSTRING(string, 1, length)    # 1-based")
print()
print("2. Character position functions:")
print("   SQL Server: CHARINDEX('char', string)       # Returns position (1-based)")
print("   Snowflake:  POSITION('char' IN string)      # Returns position (1-based)")
print("   Alternative: CHARINDEX('char', string)       # Also available in Snowflake")
print()
print("3. Length calculation:")
print("   SQL Server: Uses 0-based, so no adjustment needed")
print("   Snowflake:  Uses 1-based, so subtract 1 from position")

print("\n📋 MULTIPLE SNOWFLAKE SYNTAX OPTIONS:")
print("-" * 45)

# Option 1: Using POSITION (Snowflake preferred)
option1 = "SUBSTRING(TaskSubject, 1, POSITION('_', TaskSubject) - 1) = CherwellTicketID"
print("Option 1 (POSITION - Recommended):")
print(f"   {option1}")

# Option 2: Using CHARINDEX (SQL Server compatible)
option2 = "SUBSTRING(TaskSubject, 1, CHARINDEX('_', TaskSubject) - 1) = CherwellTicketID"
print("\nOption 2 (CHARINDEX - SQL Server compatible):")
print(f"   {option2}")

# Option 3: Using LEFT function (simpler approach)
option3 = "LEFT(TaskSubject, POSITION('_', TaskSubject) - 1) = CherwellTicketID"
print("\nOption 3 (LEFT function - Simpler):")
print(f"   {option3}")

# Option 4: Using SPLIT_PART (Snowflake specific - most elegant)
option4 = "SPLIT_PART(TaskSubject, '_', 1) = CherwellTicketID"
print("\nOption 4 (SPLIT_PART - Most elegant):")
print(f"   {option4}")

print("\n🎯 COMPLETE SNOWFLAKE QUERY EXAMPLES:")
print("-" * 42)

print("Example 1: Basic SELECT with converted logic")
complete_query1 = '''
SELECT 
    TaskSubject,
    CherwellTicketID,
    SUBSTRING(TaskSubject, 1, POSITION('_', TaskSubject) - 1) AS ExtractedID,
    CASE 
        WHEN SUBSTRING(TaskSubject, 1, POSITION('_', TaskSubject) - 1) = CherwellTicketID 
        THEN 'MATCH' 
        ELSE 'NO_MATCH' 
    END AS MatchStatus
FROM your_table_name
WHERE POSITION('_', TaskSubject) > 0;
'''
print(complete_query1)

print("Example 2: Using SPLIT_PART (Snowflake optimized)")
complete_query2 = '''
SELECT 
    TaskSubject,
    CherwellTicketID,
    SPLIT_PART(TaskSubject, '_', 1) AS ExtractedID,
    CASE 
        WHEN SPLIT_PART(TaskSubject, '_', 1) = CherwellTicketID 
        THEN 'MATCH' 
        ELSE 'NO_MATCH' 
    END AS MatchStatus
FROM your_table_name
WHERE CONTAINS(TaskSubject, '_');
'''
print(complete_query2)

print("Example 3: With error handling (NULL safety)")
complete_query3 = '''
SELECT 
    TaskSubject,
    CherwellTicketID,
    COALESCE(
        CASE 
            WHEN POSITION('_', TaskSubject) > 0 
            THEN SPLIT_PART(TaskSubject, '_', 1)
            ELSE TaskSubject
        END, 
        ''
    ) AS ExtractedID
FROM your_table_name
WHERE TaskSubject IS NOT NULL 
    AND CherwellTicketID IS NOT NULL;
'''
print(complete_query3)

print("\n📈 PERFORMANCE COMPARISON:")
print("-" * 30)
print("🥇 SPLIT_PART():     Best performance, Snowflake optimized")
print("🥈 LEFT() + POSITION(): Good performance, readable")  
print("🥉 SUBSTRING() + POSITION(): Standard performance")
print("🔄 CHARINDEX():      Compatible but not optimized")

print("\n💡 RECOMMENDED SNOWFLAKE APPROACH:")
print("="*45)
recommended = "SPLIT_PART(TaskSubject, '_', 1) = CherwellTicketID"
print(f"✅ {recommended}")
print("\nReasons:")
print("• Native Snowflake function (optimized)")
print("• Handles edge cases automatically") 
print("• More readable and maintainable")
print("• Better performance on large datasets")
print("• No need for position calculations")
print("="*60)