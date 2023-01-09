"\d \w"

import re

res = "为期40天的2023年春运大幕将正式开启"

prog1 = re.compile("[^0-9]")
prog2 = re.compile("春|大")
# ^ $
# s = "1101011980010170"
prog3 = re.compile("^[0-9]\d{2}$")
prog4 = re.compile("\d?")
prog5 = re.compile("\d{2}")
prog6 = re.compile(".")


res1 = prog6.findall(res)

print(res1)


