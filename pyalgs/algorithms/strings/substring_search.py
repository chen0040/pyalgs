from abc import ABCMeta, abstractmethod


class SubstringSearch(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def search_in(self, text):
        pass


class BruteForceSubstringSearch(SubstringSearch):
    def __init__(self, pattern):
        self.pattern = pattern

    def search_in(self, text):
        n = len(text)

        for i in range(n - len(self.pattern)):
            J = i
            for j in range(len(self.pattern)):
                k = i + j
                if text[k] != self.pattern[j]:
                    J = -1
                    break
            if J != -1:
                return J

        return -1


def char_at(text, d):
    return ord(text[d])


class RabinKarp(SubstringSearch):
    patHash = None
    Q = 1573773197
    R = 256
    M = None
    RM = None

    def __init__(self, pat):
        h = 1
        self.M = len(pat)
        for i in range(1, self.M):
            h = (h * RabinKarp.R) % RabinKarp.Q

        self.RM = h

        self.patHash = self.hash(pat, self.M)

    def hash(self, text, M):
        h = 0
        for d in range(M):
            h = (h * RabinKarp.R + char_at(text, d)) % RabinKarp.Q
        return h

    def search_in(self, text):
        text_hash = self.hash(text, self.M)
        if text_hash == self.patHash:
            return 0
        for i in range(self.M, len(text)):
            text_hash = (text_hash + RabinKarp.Q - self.RM * char_at(text, i - self.M) % RabinKarp.Q) % RabinKarp.Q
            text_hash = (text_hash * RabinKarp.R + char_at(text, i)) % RabinKarp.Q
            if text_hash == self.patHash:
                return i - self.M + 1
        return -1


class BoyerMoore(SubstringSearch):
    right = None
    R = 256
    pattern = None

    def __init__(self, pattern):
        self.pattern = pattern
        self.right = [0] * BoyerMoore.R
        for i in range(len(pattern)):
            self.right[char_at(pattern, i)] = i

    def search_in(self, text):
        n = len(text)
        m = len(self.pattern)

        skip = 1
        i = 0
        while i <= n - m:
            for j in range(m-1, -1, -1):
                if char_at(text, i+j) != char_at(self.pattern, j):
                    skip = max(1, j - self.right[char_at(text, i+j)])
                    break
                if j == 0:
                    return i
            i += skip

        return -1
