"\d \w"

import re

res = "abcdeaad"

prog1 = re.compile("a.") # ['ab', 'ac', 'ad']
prog2 = re.compile("^a.") # ['ab']

prog3 = re.compile(".*c$") # 字符串必须以c字符结尾
prog4 = re.compile("^a.*$") # ['ab']

prog5 = re.compile("a.$")
res1 = prog5.findall(res)

print(res1)


