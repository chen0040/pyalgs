from random import randint

from pyalgs.algorithms.commons.util import exchange


class KnuthShuffle(object):
    @staticmethod
    def shuffle(a):
        for i in range(1, len(a)):
            r = randint(0, i+1)
            exchange(a, r, i)
