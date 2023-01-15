import re

s1 = "bacdaef"

res = re.match("a", s1)
if res:
    print(res.group())
else:
    print(res)
res1 = re.search("a", s1)
print(res1.group())

res2 = re.findall("a", s1)
print(res2)