d = {'name1': 'id1', 'name2': 'id2', 'name3': 'id3'}
b: dict = {}
for i in d:
    b.update({d[i]: i})
print(d)
print(b)