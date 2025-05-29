class Solution(object):
    def rearrangeArray(self, arr):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(arr)
        result = [0]*n
        pos = 0
        neg = 1

        for num in arr:
            if num>=0:
                result[pos] = num
                pos+=2
            else:
                result[neg] = num
                neg+=2
        return result

        