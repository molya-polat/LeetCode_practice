class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ans = []
        if not intervals:
            return [newInterval]
        startInsert, endInsert = newInterval[0], newInterval[1]
        i = 0
        inserted = False
        while i < len(intervals):
            start, end = intervals[i][0], intervals[i][1]
            if end < startInsert or start > endInsert:
                ans.append([start, end])
                i += 1
            else:
                inserted = True
                newStart = min(start, startInsert)
                newEnd = max(end, endInsert)
                while i < len(intervals) and intervals[i][1] < endInsert:
                    i += 1
                if i < len(intervals):
                    start, end = intervals[i][0], intervals[i][1]
                    if start > endInsert:
                        newEnd = endInsert
                        ans.append([newStart, newEnd])
                        ans.append([start, end])
                    else:
                        newEnd = end
                        ans.append([newStart, newEnd])
                else:
                    ans.append([newStart, newEnd])
                i += 1
        if not inserted:
            ans.append([startInsert, endInsert])

        sorted_ans = sorted(ans)
        return sorted_ans

        # O(n) - time
        # O(n) - space