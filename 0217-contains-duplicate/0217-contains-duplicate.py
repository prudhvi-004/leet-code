class Solution(object):
    def containsDuplicate(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        seen = set()
        for num in arr:
            if num in seen:
                return True
            seen.add(num)
        return False
