class Solution(object):
    def nextPermutation(self, arr):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        i=j=len(arr)-1
        while i>0  and arr[i-1]>=arr[i]:
            i-=1
        if i == 0:
            arr.reverse()
            return
        while arr[j] <= arr[i-1]:
            j-=1
        
        arr[i-1],arr[j] = arr[j],arr[i-1]

        arr[i:] = arr[len(arr)-1:i-1:-1]
        