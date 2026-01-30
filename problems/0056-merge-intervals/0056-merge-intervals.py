class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ans = []
        intervals.sort()
        prev_start = intervals[0][0]
        prev_end = -1
        for start, end in intervals:
            if start > prev_end and prev_end != -1:
                ans.append([prev_start, prev_end])
                prev_start = start

            if end >= prev_end:
                prev_end = end

        ans.append([prev_start, prev_end])

        return ans

        # O(nlogn) - time
        # O(n) - space