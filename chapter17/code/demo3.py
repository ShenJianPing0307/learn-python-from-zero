li = [[1, 2, 3],
      [4, 5, 6],
      [7, 8, 9]]

# 元素值 + 1
# enumerate
for i in range(len(li)):
      for j in range(len(li[i])):
            li[i][j] += 1

print(li)