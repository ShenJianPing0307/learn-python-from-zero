
with open('file/1.txt', encoding="utf8") as f:
    res = f.read()
    print(res)

l = [str(i) for i in range(0, 10)]
l1 = []
for i in res:
    if i in l:
        l1.append(i)
print(l1)