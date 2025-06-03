class Solution(object):
    def findMin(self, arr):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(arr)
        smallest = arr[0]
        for i in range(1,n):
            if arr[i] < smallest:
                smallest = arr[i]
        
        return smallest
        