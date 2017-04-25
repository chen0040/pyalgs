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
                if util.less(a[j], a[k]):
                    k = j
            util.exchange(a, i, k)


class InsertionSort(object):
    @staticmethod
    def sort(a, lo=None, hi=None):
        if lo is None:
            lo = 0
        if hi is None:
            hi = len(a) - 1

        for i in range(lo, hi + 1):
            for j in reversed(range(1, i + 1)):
                if util.less(a[j], a[j - 1]):
                    util.exchange(a, j, j - 1)
                else:
                    break


class ShellSort(object):
    @staticmethod
    def sort(a):
        N = len(a)
        H = 0
        while H < N / 3:
            H = 3 * H + 1

        for h in reversed(range(1, H)):
            for i in range(h, N):
                for j in range(i, h - 1, -h):
                    if util.less(a[j], a[j - h]):
                        util.exchange(a, j, j - h)
                    else:
                        break


class MergeSort(object):
    CUTOFF = 7

    @staticmethod
    def sort(a, lo=None, hi=None):
        if lo is None:
            lo = 0
        if hi is None:
            hi = len(a) - 1

        aux = [0] * len(a)
        MergeSort._sort(a, aux, lo, hi)

    @staticmethod
    def _sort(a, aux, lo, hi):
        if lo >= hi:
            return

        if hi - lo + 1 < MergeSort.CUTOFF:
            InsertionSort.sort(a, lo, hi)
            return

        mid = lo + (hi - lo) / 2
        MergeSort._sort(a, aux, lo, mid)
        MergeSort._sort(a, aux, mid + 1, hi)
        MergeSort._merge(a, aux, lo, mid, hi)

    @staticmethod
    def _merge(a, aux, lo, mid, hi):
        i = lo
        j = mid + 1

        for k in range(lo, hi + 1):
            aux[k] = a[k]

        for k in range(lo, hi + 1):
            if i > mid:
                a[k] = aux[j]
                j += 1
            elif j > hi:
                a[k] = aux[i]
                i += 1
            elif util.less(aux[i], aux[j]):
                a[k] = aux[i]
                i += 1
            else:
                a[k] = aux[j]
                j += 1


class QuickSort(object):
    CUTOFF = 7

    @staticmethod
    def sort(a, lo=None, hi=None):
        if lo is None:
            lo = 0
        if hi is None:
            hi = len(a) - 1

        if lo >= hi:
            return

        j = QuickSort.partition(a, lo, hi)

        QuickSort.sort(a, lo, j - 1)
        QuickSort.sort(a, j + 1, hi)

    @staticmethod
    def partition(a, lo, hi):
        i = lo
        j = hi

        while True:
            while not util.less(a[lo], a[i]):
                i += 1
                if i >= hi:
                    break

            while util.less(a[lo], a[j]):
                j -= 1
                if j <= lo:
                    break

            if i >= j:
                break

            util.exchange(a, i, j)

        util.exchange(a, lo, j)
        return j


class ThreeWayQuickSort(object):
    @staticmethod
    def sort(a, lo=None, hi=None):
        if lo is None:
            lo = 0
        if hi is None:
            hi = len(a) - 1

        if lo >= hi:
            return

        i = lo
        lt = lo
        gt = hi

        while i <= gt:
            if util.less(a[i], a[lo]):
                util.exchange(a, i, lt)
                i += 1
                lt += 1
            elif util.less(a[lo], a[i]):
                util.exchange(a, i, gt)
                gt -= 1
            else:
                i += 1

        ThreeWayQuickSort.sort(a, lo, lt - 1)
        ThreeWayQuickSort.sort(a, gt + 1, hi)
