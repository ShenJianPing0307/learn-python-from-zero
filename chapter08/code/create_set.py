# 第一种，注意里面需要初始化元素，判断是字典还是集合
s = {1,}
print(s, type(s)) # <class 'set'>

# set类来创建
s1 = set()
print(s1, type(s1)) # <class 'set'>

s2 = set([1,2,3]) # set((1,2,3))
print(s2) # {1, 2, 3}