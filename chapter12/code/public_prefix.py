strs = ["flower","flow","flight"]

res = list(zip(*strs))

prefix = ""
for i in res:
    print(i)
    if len(set(i)) == 1:
        prefix += i[0]
    else:
        break
print(prefix)