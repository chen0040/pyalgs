class LSD(object):
    R = 256

    @staticmethod
    def sort(a):
        W = len(a[0])
        aux = [None] * len(a)

        for d in range(W - 1, -1, -1):
            count = [0] * (LSD.R + 1)

            for i in range(len(a)):
                count[ord(a[i][d]) + 1] += 1

            for r in range(0, LSD.R):
                count[r + 1] += count[r]

            for i in range(len(a)):
                aux[count[ord(a[i][d])]] = a[i]
                count[ord(a[i][d])] += 1

            for i in range(len(a)):
                a[i] = aux[i]


class MSD(object):

    R = 256

    @staticmethod
    def sort(a):
        MSD._sort(a, 0, len(a)-1, 0)

    @staticmethod
    def _sort(a, lo, hi, d):
        if hi - lo <= 0:
            return

        count = [0] * (MSD.R+2)
        aux = [None] * (hi - lo + 1)

        for i in range(lo, hi+1):
            count[MSD.char_at(a[i], d) + 2] += 1

        for r in range(0, MSD.R):
            count[r+1] += count[r]

        for i in range(lo, hi+1):
            aux[count[MSD.char_at(a[i], d) + 1]] = a[i]
            count[MSD.char_at(a[i], d) + 1] += 1

        for i in range(lo, hi+1):
            a[i] = aux[i-lo]

        for r in range(MSD.R):
            MSD._sort(a, lo + count[r], lo + count[r+1] -1, d+1)

    @staticmethod
    def char_at(text, d):
        if len(text) <= d+1:
            return -1
        return ord(text[d])