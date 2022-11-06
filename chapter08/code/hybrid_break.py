

for i in range(3):
    for j in range(3):
        print("内层",i, j)
        if j >= 2:
            break
    print("外层",i)
"""
"内层" 0 0
"内层" 0 1
"内层" 0 2
"外层" 0

"内层" 1 0
"内层" 1 1
"内层" 1 2
"外层" 1

...
"""

for i in range(3):
    for j in range(3):
        print("内层",i, j)
        if j >= 2:
            break
    print("外层",i)
    if i >= 1:
        break
"""
"内层" 0 0
"内层" 0 1
"内层" 0 2
"外层" 0

"内层" 1 0
"内层" 1 1
"内层" 1 2
"外层" 1
"""