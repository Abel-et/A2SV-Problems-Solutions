class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[0], -x[1]))

        max_end = 0
        remaining = 0 

        for start , end in intervals:
            if end > max_end:
                max_end = end
                remaining += 1
        return remaining