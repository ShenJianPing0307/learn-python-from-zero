"\d \w"

import re

res = "abcdeaad"

prog1 = re.compile("a.?") # ['ab', 'aa']
prog2 = re.compile("^a.?") # ['ab']
prog21 = re.compile("a.?$") # ['ab']

prog3 = re.compile("a.+?") # ['abcdeaad']
prog4 = re.compile("^a.*$") # ['ab']

prog5 = re.compile("a.$")
res1 = prog3.findall(res)

print(res1)


