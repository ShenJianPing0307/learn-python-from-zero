ll = [1, 2, 3]


def a(li):
    li.extend([4, 5, 6])


res = a(ll)

print(res) # None
print(ll) # [1,2,3,4,5,6]

def b():

    for i in range(10):
        for j in range(10):
            if i > 3:
                return
        print(i)

b()
"""
0
1
2
3
"""