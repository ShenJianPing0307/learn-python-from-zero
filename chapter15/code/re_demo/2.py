"\d \w"

import re

with open('file/1.txt', encoding="utf8") as f:
    res = f.read()
    print(res)

prog = re.compile("\d{3}")

res1 = prog.findall(res)

print(res1)
