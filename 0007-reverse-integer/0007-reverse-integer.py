class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0

        num = ""
        neg = x < 0
        x = abs(x)
        
        while x != 0:
            quot = x % 10
            num += str(quot)
            x = x // 10
        
        result = int(num)
        if neg:
            result = -result

        if result < -2**31 or result > 2**31 - 1:
            return 0

        return result
