lst1 = [2, 3, 5, 8, 9, 13, 25, 33, 44, 52, 64, 73, 81, 99]


def bin_search(lst, item):
    left, right = 0, len(lst) - 1
    while left <= right:
        mid = (left + right) // 2
        if item == lst[mid]:
            return print(f'Элемент {item} найден, позиция: {mid}')
        elif item > lst[mid]:
            left = mid + 1
        else:
            right = mid - 1
    return print(f'Элемент {item} не найден!')

print(bin_search(lst1, 99))
