l1 = [1, 2, 3]
l2 = [4, 5, 6]
l3 = [7, 8, 9]

"""
{1:4,2:5,3:6,4:7,5:8,6:9}
已知l1,求l3
"""
l_dict = {}


def generate_dict(l1, l2):
    for idx, val in enumerate(l1):
        l_dict[val] = l2[idx]


generate_dict(l1, l2)
generate_dict(l2, l3)
print(l_dict)

ll = {1: 4, 2: 5, 3: 6, 4: 7, 5: 8, 6: 9}

value = []
for k, v in ll.items():
    if k in l1:
        value.append(ll[v])
print(value)
