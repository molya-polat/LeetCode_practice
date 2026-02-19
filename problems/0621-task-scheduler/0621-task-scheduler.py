from collections import deque
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        diction = defaultdict(int)
        for t in tasks:
            diction[t] += 1

        max_heap = []
        for task, count in diction.items():
            heapq.heappush(max_heap, (-count))
        
        time = 0
        while max_heap:
            update_frq = []
            current_time = 0
            cycle = n + 1
            while cycle > 0 and max_heap:
                if max_heap:
                    freq = -heapq.heappop(max_heap)
                    if freq > 1:
                        update_frq.append(freq - 1)
                cycle -= 1
                current_time += 1
            
            for fr in update_frq:
                heapq.heappush(max_heap, -fr)
                
            time += current_time if not max_heap else n + 1
        
        return time