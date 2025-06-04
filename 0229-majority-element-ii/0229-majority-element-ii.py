class Solution(object):
    def majorityElement(self,arr):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(arr)
        freq = {}

        for num in arr:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
        result = []
        for num,value in freq.items():
            if value > n/3:
                result.append(num)
        
        return result

        