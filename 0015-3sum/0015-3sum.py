class Solution(object):
    def threeSum(self, arr):
        arr.sort()
        n = len(arr)
        output = []

        for i in range(n - 2):
            if i > 0 and arr[i] == arr[i - 1]:
                continue

            j = i + 1
            k = n - 1

            while j < k:
                total = arr[i] + arr[j] + arr[k]

                if total == 0:
                    output.append([arr[i], arr[j], arr[k]])
                    j += 1
                    k -= 1

                    while j < k and arr[j] == arr[j - 1]:
                        j += 1
                    while j < k and arr[k] == arr[k + 1]: 
                        k -= 1

                elif total < 0:
                    j += 1
                else:
                    k -= 1

        return output
