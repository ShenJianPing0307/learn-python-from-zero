s1 = "hello"

# 索引 + 拼接字符串
s2 = s1[0]
s3 = s1[1]
print(s2 + s3)
print("%s%s" % (s2, s3))

# 切片 左取右不取[) 正向取值
s5 = s1[0:2]
print(s5)

# 切片 右取左不取(] 负向取值
s6 = s1[-5:-3]
print("s6", s6)

# 切片 混合取值
s7 = s1[0:-3]
print("s7", s7)

# 步长切片 hell
s8 = s1[0:3:2]
print("s8", s8)

# 切片的其它情况
s9 = s1[::]  # 取所有的字符
print("s9", s9)
s10 = s1[1:]
print("s10", s10)



