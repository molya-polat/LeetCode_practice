import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals, key = lambda x: x[0])
        heap = []
        for start, end in intervals:
            if not heap:
                heapq.heappush(heap, end)
            else:
                earliest_end = heap[0]
                if earliest_end <= start:
                    heapq.heappop(heap)
                heapq.heappush(heap, end)
        
        return len(heap)

        # O(nlogn) - time
        # O(n) - space





















        # result = 0
        # intervals.sort(key=lambda x: x[0])
        # rooms_end = []
        # for i, interval in enumerate(intervals):
        #     if i == 0:
        #         result += 1
        #         rooms_end.append(interval[1])
        #     else:
        #         if interval[0] < min(rooms_end):
        #             result += 1
        #             rooms_end.append(interval[1])
        #         else:
        #             index_min = rooms_end.index(min(rooms_end))
        #             rooms_end[index_min] = interval[1]

        # return result

        # # O(n * n) - time
        # # O(n) - memory