class Solution(object):
    def moveZeroes(self, arr):
        """
        :type arr: List[int]
        :rtype: None (modifies arr in-place)
        """
        pos = 0  

        for i in range(len(arr)):
            if arr[i] != 0:
                arr[pos], arr[i] = arr[i], arr[pos]
                pos += 1

