class Solution:
    def longestArithmetic(self, nums: List[int]) -> int:
        diff2intervals = {}
        max_length = 0
        current_diff = nums[1] - nums[0]
        start = 0

        for i in range(1, len(nums)):
            if nums[i] - nums[i - 1] != current_diff:
                if current_diff not in diff2intervals:
                    diff2intervals[current_diff] = []
                diff2intervals[current_diff].append((start, i - 1))
                max_length = max(max_length, i - start)
                start = i - 1
                current_diff = nums[i] - nums[i - 1]
            max_length = max(max_length, i - start + 1)

        def isValid(k):
            return 0 <= k < len(nums)

        def checkNeighbors(start, end, diff):
            length = end - start + 1
            if isValid(start - 2) and nums[start] - nums[start - 2] == 2 * diff:
                length += 2
                return length
            
            if isValid(end + 2) and nums[end + 2] - nums[end] == 2 * diff:
                length += 2 
            return length


        if current_diff not in diff2intervals:
            diff2intervals[current_diff] = []
        diff2intervals[current_diff].append((start, len(nums) - 1))
        max_length = max(max_length, len(nums) - start)
        max_length += 1

        for diff, intervals in diff2intervals.items():
            for i in range(len(intervals)):
                a, b = intervals[i][0], intervals[i][1]
                if i > 0 and a - intervals[i - 1][1] == 2 and nums[a] - nums[intervals[i - 1][1]] == diff * 2:
                    max_length = max(max_length, intervals[i][1] - intervals[i - 1][0] + 1)
                length = checkNeighbors(intervals[i][0], intervals[i][1], diff)
                max_length = max(max_length, length)

        if max_length > len(nums):
            return len(nums)
        return max_length

        # O(n) - time
        # O(n) - space