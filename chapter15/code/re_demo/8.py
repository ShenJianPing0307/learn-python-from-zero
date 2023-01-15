import re

text1 = "新华社北京1月13日电题：2023年春运迎“大考”"

reg = re.compile(".*?(\d+).*?")

res = re.findall(reg, text1)
print(res)