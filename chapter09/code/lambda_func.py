
def add(x, y):
    return x+y

add = lambda x,y : x + y

print(add(1,2))

def add(x, y):
    return lambda :x+y
print(add(1,2)())