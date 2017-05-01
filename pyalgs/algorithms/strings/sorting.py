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
