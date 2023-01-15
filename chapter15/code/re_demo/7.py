import re


text = "110101198001017032"
reg = re.compile("^[1-9]\d{16}[1-9X]")

res = re.findall(reg, text)
print(res)
