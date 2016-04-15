class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        return self.numDecodingsHelper(s, {})

    def numDecodingsHelper(self, s, cache):
        if s in cache: return cache[s]

        if len(s) == 0: return 0

        if len(s) == 1:
            if int(s) == 0: return 0
            else: return 1

        if len(s) == 2:
            if int(s) < 10: return 0
            elif int(s) == 10: return 1
            elif int(s) <= 19: return 2
            elif int(s) == 20: return 1
            elif int(s) <= 26: return 2
            elif int(s[1]) == 0: return 0
            else: return 1

        is_valid_char = True if int(s[0]) != 0 else False
        is_valid_chars = True if len(s) > 1 and 9<int(s[0:2]) and int(s[0:2]) <= 26 else False

        if is_valid_char and is_valid_chars:
            res = self.numDecodingsHelper(s[1:], cache) + self.numDecodingsHelper(s[2:], cache)

        elif is_valid_char and not is_valid_chars:
            res = self.numDecodingsHelper(s[1:], cache)

        elif not is_valid_char and is_valid_chars:
            res = self.numDecodingsHelper(s[2:], cache)

        else:
            res = 0

        cache[s] = res
        return cache[s]
