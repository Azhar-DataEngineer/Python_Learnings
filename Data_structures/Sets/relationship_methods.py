a = {10,20,30,40}

b = {30,40,50,60}

print(a.issubset(b))


x = {30,40}
y = {30,40,50,60}

print(x.issubset(y))
# True as all items of x are in y

print(y.issuperset(x))
# True as all items of x are in y