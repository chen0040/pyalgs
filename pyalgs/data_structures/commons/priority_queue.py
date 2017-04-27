from pyalgs.algorithms.commons.util import less, exchange, greater


class MinPQ(object):
    pq = None
    N = 0

    def __init__(self, capacity=None):
        if capacity is None:
            capacity = 10
        self.pq = [0] * capacity

    def enqueue(self, key):
        self.N += 1
        if self.N == len(self.pq):
            self.resize(len(self.pq) * 2)

        self.pq[self.N] = key
        self.swim(self.N)

    def swim(self, k):
        while k > 1:
            parent = k // 2
            if less(self.pq[k], self.pq[parent]):
                exchange(self.pq, k, parent)
                k = parent
            else:
                break

    def del_min(self):
        if self.is_empty():
            return None

        key = self.pq[1]
        exchange(self.pq, 1, self.N)
        self.N -= 1
        if self.N == len(self.pq) // 4:
            self.resize(len(self.pq) // 2)

        self.sink(self.pq, 1, self.N)
        return key

    @staticmethod
    def sink(tmp, k, n):

        while k * 2 <= n:
            child = k * 2
            if child < n and less(tmp[child + 1], tmp[child]):
                child = child + 1
            if less(tmp[child], tmp[k]):
                exchange(tmp, child, k)
                k = child
            else:
                break

    def resize(self, new_size):
        tmp = [0] * new_size
        for k in range(min(new_size, len(self.pq))):
            tmp[k] = self.pq[k]
        self.pq = tmp

    def is_empty(self):
        return self.N == 0

    def size(self):
        return self.N

    def iterate(self):
        tmp = [0] * (self.N + 1)
        for k in range(self.N + 1):
            tmp[k] = self.pq[k]

        n = self.N
        while n >= 1:
            key = tmp[1]
            exchange(tmp, 1, n)
            n -= 1
            self.sink(tmp, 1, n)
            yield key

    @staticmethod
    def create():
        return MinPQ()


class MaxPQ(object):
    pq = None
    N = 0

    def __init__(self, capacity=None):
        if capacity is None:
            capacity = 10
        self.pq = [0] * capacity

    def enqueue(self, key):
        if self.N == len(self.pq):
            self.resize(len(self.pq) * 2)
        self.N += 1
        self.pq[self.N] = key
        self.swim(self.N)

    def swim(self, k):
        while k > 1:
            parent = k // 2
            if greater(self.pq[k], self.pq[parent]):
                exchange(self.pq, k, parent)
                k = parent
            else:
                break

    def del_max(self):
        if self.is_empty():
            return None

        key = self.pq[1]
        exchange(self.pq, 1, self.N)
        self.N -= 1
        if self.N == len(self.pq) // 4:
            self.resize(len(self.pq) // 2)

        self.sink(self.pq, 1, self.N)
        return key

    @staticmethod
    def sink(tmp, k, n):

        while k * 2 <= n:
            child = k * 2
            if child < n and greater(tmp[child + 1], tmp[child]):
                child = child + 1
            if greater(tmp[child], tmp[k]):
                exchange(tmp, child, k)
                k = child
            else:
                break

    def resize(self, new_size):
        tmp = [0] * new_size
        for k in range(min(new_size, len(self.pq))):
            tmp[k] = self.pq[k]
        self.pq = tmp

    def is_empty(self):
        return self.N == 0

    def size(self):
        return self.N

    def iterate(self):
        tmp = [0] * (self.N + 1)
        for k in range(self.N + 1):
            tmp[k] = self.pq[k]

        n = self.N
        while n >= 1:
            key = tmp[1]
            exchange(tmp, 1, n)
            n -= 1
            self.sink(tmp, 1, n)
            yield key

    @staticmethod
    def create():
        return MaxPQ()


class IndexMinPQ(object):

    keys = None
    pq = None
    qp = None
    N = 0

    def __init__(self, size):
        self.keys = [None] * (size+1)
        self.pq = [0] * (size+1)
        self.qp = [0] * (size+1)

    def insert(self, index, key):
        self.keys[index] = key
        self.N += 1
        self.pq[self.N] = index
        self.qp[index] = self.N

        self.swim(self.N)

    def decrease_key(self, index, key):
        self.keys[index] = key
        k = self.qp[index]
        self.swim(k)

    def contains_index(self, index):
        return self.keys[index] is not None

    def swim(self, k):
        while k > 1:
            parent = k // 2
            if less(self.keys[self.pq[k]], self.keys[self.pq[parent]]):
                exchange(self.pq, k, parent)
                self.qp[self.pq[k]] = k
                self.qp[self.pq[parent]] = parent
                k = parent
            else:
                break

    def get(self, index):
        return self.keys[index]

    def min_key(self):
        return self.keys[self.pq[1]]

    def del_min(self):
        index = self.pq[1]
        exchange(self.pq, 1, self.N)
        self.qp[self.pq[1]] = 1
        self.qp[self.pq[self.N]] = self.N

        self.N -= 1
        self.sink(1)

        return index

    def sink(self, k):
        while 2 * k <= self.N:
            child = 2 * k
            if child < self.N and less(self.keys[self.pq[child]], self.keys[self.pq[child+1]]):
                child = child+1
            if less(self.keys[self.pq[child]], self.keys[self.pq[k]]):
                exchange(self.pq, k, child)
                self.qp[self.pq[k]] = k
                self.qp[self.pq[child]] = child
                k = child
            else:
                break

    def is_empty(self):
        return self.N == 0

    def size(self):
        return self.N
