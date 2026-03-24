class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:
        workerTimes.sort()
        nextW = [[x, 1, i] for i,x in enumerate(workerTimes)]
        heapq.heapify(nextW)
        m = 1
        seconds = 0
        current_s = workerTimes[0]
        while m <= mountainHeight:
            workTime, ct, i = heapq.heappop(nextW)
            current_s = workTime
            workTime += (ct + 1) * workerTimes[i]
            heapq.heappush(nextW, [workTime, ct + 1, i])

            m += 1
            seconds = max(seconds, current_s)
        
        return seconds

        # O(n logn) - time
        # O(n) - space

            
















        k = mountainHeight // length
        r = mountainHeight % length
        arr = [i for i in range(1, k + 1)]
        maxW1 = workerTimes[-1]
        seconds = maxW1 * sum(arr)
        if r != 0:
            maxW2 = max(workerTimes[:r])
            # print(seconds, workerTimes[r-1])
            seconds = max(seconds, maxW2 * (sum(arr) + k + 1))
        return seconds