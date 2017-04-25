from util import is_sorted, less
from sorting import MergeSort

class BinarySelection(object):
    @staticmethod
    def index_of(a, x, lo=None, hi=None):
        if not is_sorted(a):
            raise ValueError('array must be sorted before running selection')

        if lo is None:
            lo = 0
        if hi is None:
            hi = len(a)-1

        while lo <= hi:
            mid = lo + (hi - lo) / 2
            if less(x, a[mid]):
                hi = mid-1
            elif less(a[mid], x):
                lo = mid+1
            else:
                return mid

        return -1