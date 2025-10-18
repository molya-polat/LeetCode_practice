class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        validSelections = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                newNums = nums.copy()
                curr = i
                direction = 1
                while curr >= 0 and curr < len(newNums):  # right side
                    if newNums[curr] != 0:
                        newNums[curr] -= 1
                        direction = -direction
                    curr += direction
                if len(set(newNums)) == 1:
                    validSelections += 1
                newNums = nums.copy()
                curr = i
                direction = -1
                while curr >= 0 and curr < len(newNums):  # left side
                    if newNums[curr] != 0:
                        newNums[curr] -= 1
                        direction = -direction
                    curr += direction
                if len(set(newNums)) == 1:
                    validSelections += 1

                
        return validSelections

        # O(n^2) - time compl
        # O(n) - space compl