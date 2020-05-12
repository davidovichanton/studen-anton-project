def find(l, x):
    for i, item in enumerate(l):
        if item == x:
            return i

    return -1

l = [1, 2, 3, 4, 5]
print(find(l, 2))
print(find(l, 4))
print(find(l, 10))


l1 = [1, 2, 3, 5, 2, 1, 7]
l2 = [2, 3, 4, 9, 7]

for i1 in l1:
    if find(l2, i1) != -1:
        print(i1)
