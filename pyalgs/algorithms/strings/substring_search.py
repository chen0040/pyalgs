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
