
f = open(file="./1.csv", mode="r")
# res = f.readline()
# print(res)
# while True:
#     line = f.readline()
#     if not line:
#         break
#     print(line)

res = f.readlines()
print(res)
