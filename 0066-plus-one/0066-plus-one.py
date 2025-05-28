class Solution(object):
    def plusOne(self, arr):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        maxi = ""
        for i in arr:
            maxi += str(i)
        
        max_one = int(maxi) + 1 
        result = []
        for i in str(max_one):
            result.append(int(i))

        return result