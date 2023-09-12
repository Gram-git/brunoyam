l: list = [1, 3, 4, 5, 1, 2, 'hello', 'world', 2, 0, 'hello']
l2: list = []
for i in l:
    if l.count(i) > 1 and i not in l2:
        l2.append(i)
print(l2)