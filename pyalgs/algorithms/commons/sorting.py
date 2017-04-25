import util


class SelectionSort(object):
    """ Order of Growth: N^2
    """
    @staticmethod
    def sort(a):
        N = len(a)
        for i in range(N):
            k = i
            for j in range(i + 1, N):
                if a[k] > a[j]:
                    k = j
            util.exchange(a, i, k)
