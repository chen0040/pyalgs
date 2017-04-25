def less(a, b):
    return cmp(a, b) < 0

def greater(a, b):
    return cmp(a, b) > 0

def exchange(a, i, j):
    tmp = a[j]
    a[j] = a[i]
    a[i] = tmp


def is_sorted(a):
    if len(a) <= 1:
        return True
    for i in range(1, len(a)):
        if less(a[i], a[i-1]):
            return False
    return True

