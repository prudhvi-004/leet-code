class Solution(object):
    def longestConsecutive(self, arr):
        """
        :type nums: List[int]
        :rtype: int
        """
        arr_set = set(arr)
        longest = 0

        for i in arr_set:
            if i-1 not in arr_set:
                current = i
                count = 1

                while current+1 in arr_set:
                    current+=1
                    count+=1
                
                longest  = max(longest,count)
        return longest
        