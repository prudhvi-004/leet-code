class Solution(object):
    def singleNumber(self, arr):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(arr)
        fre = {}
        for num in arr:
            if num in fre:
                fre[num] += 1
            else:
                fre[num] = 1
        
        for num, val in fre.items():
            if val == 1:
                return num
            