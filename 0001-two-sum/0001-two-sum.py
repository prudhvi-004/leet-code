class Solution(object):
    def twoSum(self, arr, target):
        n = len(arr)
        left = 0
        right = n - 1

        arr_with_index = list(enumerate(arr))
        arr_with_index.sort(key=lambda x: x[1])  
        while left < right:
            sum_val = arr_with_index[left][1] + arr_with_index[right][1]
            if sum_val > target:
                right -= 1
            elif sum_val < target:
                left += 1
            else:
                return [arr_with_index[left][0], arr_with_index[right][0]]
