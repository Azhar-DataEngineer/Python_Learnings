domains = ['www.google.com',
           'openapi.com',
           'localhost',
           'WWW.DATAWITHBARA.COM'
           ]
cleaned = [
    # data transformation
    d.lower().replace('www.', '')   
    # for loop
    for d in domains 
    # data filtering
    if '.' in d
]

print(cleaned)