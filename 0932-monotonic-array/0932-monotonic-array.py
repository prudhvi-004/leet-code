class Solution(object):
    def isMonotonic(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        increasing = decreasing = True
        
        for i in range(len(arr) - 1):
            if arr[i] < arr[i + 1]:
                decreasing = False
            elif arr[i] > arr[i + 1]:
                increasing = False
        
        return increasing or decreasing
