class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k%n
        temp = nums[n-k:]

        for i in range(n-k-1,-1,-1):
            nums[i+k] = nums[i]
        for j in range(k):
            nums[j] = temp[j]
        return nums
