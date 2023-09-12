from random import randint

n = 5
m = [[randint(0,100) for i in range(n)] for j in range(n)]
max1: int = 0
for i in m:
    for j in i:
        if j > max1:
            max1 = j
print(max1)