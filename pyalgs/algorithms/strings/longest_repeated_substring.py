
class LongestRepeatedSubstringSearch(object):
    @staticmethod
    def lrs(text, pattern):
        n = len(text)
        a = [''] * n
        for i in range(0, n):
            a[i] = text[i:]

        sorted(a)

        max_len = 0
        j = -1
        for i in range(0, n):
            l = LongestRepeatedSubstringSearch.lcp(a[i], pattern)
            if l > max_len:
                j = i
                max_len = l

        return (j, max_len)

    @staticmethod
    def lcp(text, pattern):
        i = 0
        for i in range(min(len(text), len(pattern))):
            if text[i] != pattern[i]:
                return i
        return i
