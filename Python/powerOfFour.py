class Solution(object):
    def isPowerOfFour(self, num):
        if num < 0: return False

        while True:
            if num == 1: return True
            if num == 0: return False

            if num % 4 != 0: return False
            num /= 4