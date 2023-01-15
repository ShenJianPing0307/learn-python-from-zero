import re
s = "abc12def13jk"

# s1 = s.replace("12", "gh").replace("13", "gh")
# print(s1)

s1 = re.sub("\d+", "gh", s)
print(s1)
