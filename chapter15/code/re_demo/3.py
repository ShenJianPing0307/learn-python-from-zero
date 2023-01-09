"\d \w"

import re

with open('file/1.txt', encoding="utf8") as f:
    res = f.read()
    print(res)

prog = re.compile("[a-z0-9]")

res1 = prog.findall(res)

print(res1)
def f1(a):
    a.findall()

f1(re.compile("[a-z0-9]"))

