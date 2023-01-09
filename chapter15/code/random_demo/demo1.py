import random


def generate_code():
    """5个数字字母组合的验证码"""

    l1 = [str(i) for i in range(0, 10)]
    l2 = [i for i in range(65, 91)]

    l3 = random.sample(l1, 3)
    l4 = random.sample(l2, 2)
    l4 = [chr(j) for j in l4]

    l3.extend(l4)

    res = "".join(l3)
    return res


res = generate_code()
print(res)
