strs = ["flower","flow","flight"]
"""
[f, f, f]
[l, l, l]
...
"""

res = zip(*strs) # *args args=[1,2,3]

res1 = ""
for i in res:
    if len(set(i)) == 1: # ('f',)
        res1 += i[0]
    else:
        break

print(res1) # fl

