class Solution(object):
    def maxSubArray(self, arr):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxi = arr[0]
        cur = 0

        for num in arr:
            temp = cur +num
            if temp>num:
                cur = temp
            else:
                cur = num
            
            maxi = max(maxi,cur)
        return maxi


