import re

text1 = "新华社北京1月13日电题：2023年春运迎“大考”"

reg = re.compile(".*?(\d+).*?")


res = reg.match(text1).group()
res1 = reg.search(text1).group()

print(res)
print(res1)