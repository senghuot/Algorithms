class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self.climbStairsHelper(n, {})

    def climbStairsHelper(self, n, cache):

        if n in cache: return cache[n]

        if n < 0: return 0

        if n == 0: return 1

        cache[n] = self.climbStairsHelper(n-1, cache) + self.climbStairsHelper(n-2, cache)

        return cache[n]
