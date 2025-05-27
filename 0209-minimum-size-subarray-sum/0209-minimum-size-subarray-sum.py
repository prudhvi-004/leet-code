class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        left = 0
        right = 0
        cur_sum = 0

        min_len = n + 1

        while right < n:
            cur_sum += nums[right]

            while cur_sum >= target and left <= right:
                min_len = min(min_len, right - left + 1)
                cur_sum -= nums[left]
                left += 1

            right += 1

        return 0 if min_len == n + 1 else min_len
