class Solution(object):
    def majorityElement(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """

        candidate = None
        count = 0

        for num in arr:
            if count == 0:
                candidate = num
            count += 1 if num == candidate else -1

        if arr.count(candidate) > len(arr) // 2:
            return candidate
        return -1
