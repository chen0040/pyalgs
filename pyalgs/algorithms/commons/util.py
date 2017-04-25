def less(a, b):
    return a < b

def exchange(a, i, j):
    tmp = a[j]
    a[j] = a[i]
    a[i] = tmp