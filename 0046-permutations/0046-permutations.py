class Solution(object):
    def permute(self, arr, f=0):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if f >= len(arr):
            return [arr[:]]
        res = []
        for s in range(f, len(arr)):
            arr[f], arr[s] = arr[s], arr[f]
            res += self.permute(arr, f + 1)
            arr[f], arr[s] = arr[s], arr[f]
        return res
