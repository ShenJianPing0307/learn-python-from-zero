import random

l1 = [1,2,3]
l2 = ["a","c"]
m = random.choice(l1)
n = random.choice(l2)

print(m,n)
pas = "123456789abcdefABCD"

res = ""
for i in range(6):
    res += random.choice(pas)
print(res)
