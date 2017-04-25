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
    def sort(a):
        N = len(a)
        for i in range(N):
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
