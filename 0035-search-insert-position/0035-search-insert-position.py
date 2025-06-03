class Solution(object):
    def searchInsert(self, arr, target):
        """
        :type arr: List[int]
        :type target: int
        :rtype: int
        """
        n = len(arr)
        for i in range(n):
            if arr[i] >= target:
                return i
        return n
