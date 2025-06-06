class Solution(object):
    def merge(self, arr1, m, arr2, n):
        left = 0
        right = 0
        index = 0
        arr3 = [0] * (m + n)

        while left < m and right < n:
            if arr1[left] <= arr2[right]:
                arr3[index] = arr1[left]
                left += 1
                index += 1
            else:
                arr3[index] = arr2[right]
                right += 1
                index += 1

        while left < m:
            arr3[index] = arr1[left]
            left += 1
            index += 1

        while right < n:
            arr3[index] = arr2[right]
            right += 1
            index += 1

        for i in range(m + n):
            arr1[i] = arr3[i]
