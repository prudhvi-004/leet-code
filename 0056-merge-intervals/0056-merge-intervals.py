class Solution(object):
    def merge(self, intervals):
        if not intervals:
            return []

        intervals.sort()
        merged = [intervals[0]]

        for i in range(1, len(intervals)):
            prev = merged[-1]
            curr = intervals[i]

            if curr[0] <= prev[1]:
                prev[1] = max(prev[1], curr[1])
            else:
                merged.append(curr)

        return merged
