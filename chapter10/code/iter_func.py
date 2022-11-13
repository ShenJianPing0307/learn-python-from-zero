
l1 = [1,2,3]

res = iter(l1)

print(next(res)) # next()  ==  __next__
print(res)

def reduce(function, iterable, initializer=None):
    it = iter(iterable) # [1,2,3]
    if initializer is None:
        value = next(it) # 1
    else:
        value = initializer
    for element in it: # 2, 3
        value = function(value, element) # 1 , 2
    return value