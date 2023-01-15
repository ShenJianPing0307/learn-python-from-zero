import re
# 方法一 [a,b,c,d,e]
s1 = "a-b_c-d_e"

# res = s1.split("_")
# print(res)
# res1 = []
# for i in res:
#     res1.extend(i.split("-"))
# print(res1)

# 方法二  cookbook
# res = re.split("_|-", s1)
res = re.split("[_-]", s1)

print(res)
