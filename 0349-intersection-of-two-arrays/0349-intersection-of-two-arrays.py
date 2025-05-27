class Solution(object):
    def intersection(self, num1, num2):
        num1.sort()
        num2.sort()

        n1 = len(num1)
        n2 = len(num2)

        i = 0
        j = 0

        result = []

        while i<n1 and j<n2:
            if num1[i] == num2[j]:
                if not result or result[-1]!=num1[i]:
                    result.append(num1[i])
                i+=1
                j+=1
            elif num1[i]<num2[j]:
                i+=1
            else:
                j+=1
        
        return result