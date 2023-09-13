m: list = [56, 9, 11, 2, 9, 3]


def sort_max(arg1):
    exc = []
    result = ''
    while len(exc) < len(arg1):
        var1: int = 0
        for i in arg1:
            if i not in exc:
                if len(str(i)) == len(str(var1)):
                    if var1 < i:
                        var1 = i
                elif len(str(i)) > len(str(var1)):
                    x = int(str(var1) + (len(str(i)) - len(str(var1))) * '9')
                    if x < i:
                        var1 = i
                elif len(str(i)) < len(str(var1)):
                    x = int(str(i) + (len(str(var1)) - len(str(i))) * '9')
                    if var1 < x:
                        var1 = i
        for i in range(arg1.count(var1)):
            exc.append(var1)
    for i in exc:
        result += str(i)
    return int(result)


print(m)
print(sort_max(m))
