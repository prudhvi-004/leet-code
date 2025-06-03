class Solution(object):
    def permuteUnique(self, arr, f=0):
        """
        :type arr: List[int]
        :rtype: List[List[int]]
        """
        if f >= len(arr):
            return [arr[:]]

        res = []
        used = set() 
        for s in range(f, len(arr)):
            if arr[s] in used:
                continue
            used.add(arr[s])
            arr[f], arr[s] = arr[s], arr[f]
            res += self.permuteUnique(arr, f + 1)
            arr[f], arr[s] = arr[s], arr[f]
        return res
