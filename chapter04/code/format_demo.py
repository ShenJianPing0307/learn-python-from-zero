s1 = "{}-{}"
s2 = s1.format("hello","world")
print(s2)

s3 = "{a}:{b}"
print(s3.format(b="world", a="hello"))

# 您好,世界,hello,world  先是顺序后是关键字
s5 = "{a}{},{b}{}"
print(s5.format("世界","world", a="您好", b="hello"))

str
