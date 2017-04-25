def less(a, b):
    return cmp(a, b) < 0


def exchange(a, i, j):
    tmp = a[j]
    a[j] = a[i]
    a[i] = tmp
