def max(l, *b,):
    m = float("-inf")

    for i in l:
        if i > m:
            m = i
    return m

l1 = [1, 2 , 3, 4322, 746387]

m1 = max(l1)

l2 = list(range(3, 7))

m2 = max(l2)

print(f"{l1=} {m1=} {l2=} {m2=}")
if m1 > m2:
    print(l1)
else:
    print(l2)


def newfunc(a, *b, **c):
    return max(a, *b)


f = newfunc([1])
print(f)
