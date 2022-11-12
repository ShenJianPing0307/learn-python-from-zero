# lis = ['%s%s=%s'%(i,j,ij) for i in range(1,10) for j in range(i,10)]
def the_9_9_list():
    for i in range(1, 10):
        for j in range(1, 10):
            print("%d * %d = %d" % (i, j, i * j))


# the_9_9_list()

"""
1 * 1 = 1
1 * 2 = 2 2 * 1 =2
...
"""


def the_9_9_list1():
    for i in range(1, 10):
        for j in range(1, i + 1):
            print("{} * {} = {}".format(j, i, i * j), end=" ")
        print()


# the_9_9_list1()
"""
1 * 1 = 1 
1 * 2 = 2      
...
1 * 10 = 10 
"""

import random

li = []
for i in range(1000):
    li.append(i)
random.shuffle(li) # 打乱顺序
print(li)


# for i in range(len(li)):
#     for j in range(i+1, len(li)):
#         if li[i] <= li[j]:
#             li[i], li[j] = li[j], li[i]
#
# print(li)
a = [111, 63, 364, 525] # 111 63  --> 63 111 364 525
                        # 63 111 364 525
                        # 63 111 364 525
for i in range(len(li)-1):
    for j in range(len(li)-i-1):
        if li[j] > li[j+1]:
            li[j], li[j+1] = li[j+1], li[j]


