class Solution(object):
    def subarraySum(self, arr, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        prefix = {}
        prefix[0] = 1
        count = 0
        current = 0

        for num in arr:
            current += num
            target = current - k

            if target in prefix:
                count+=prefix[target]
            
            if current in prefix:
                prefix[current]+=1
            else:
                prefix[current]=1
        
        return count


        