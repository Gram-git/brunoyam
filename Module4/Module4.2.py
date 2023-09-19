lst1 = [-4, 1, 3, 4, 0, 6, 3, -8]


def insertion_sort(lst):
    n = len(lst)
    for i in range(1,n):
        for j in range(i,0,-1):
            if lst[j] < lst[j-1]:
                lst[j],lst[j-1]=lst[j-1],lst[j]
            else:
                break

print(insertion_sort(lst1),lst1)
