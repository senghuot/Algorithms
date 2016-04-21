class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """

        if n == 2: return 1
        if n == 3: return 2

        res = 1
        while n > 0:
            if n == 2:
                return res * 2
            if n == 4:
                return res * 4

            res = res * 3
            n = n - 3

        return res