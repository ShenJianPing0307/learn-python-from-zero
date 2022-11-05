def hash_code(key):
    a = 1
    b = 2
    c = 3
    if key == 'ab':
        res = a + b
    elif key == 'bc':
        res = b + c
    else:
        res = a + c
    return res % 3


hash_table = [None] * 3
print(hash_table)

"""
"ab": 1, "bc": 2, "ca": 3
"""
idx = hash_code("ab")
hash_table[idx] = 1
print(hash_table)
idx = hash_code("bc")
hash_table[idx] = 2
print(hash_table)
idx = hash_code("ca")
hash_table[idx] = 3
print(hash_table)
