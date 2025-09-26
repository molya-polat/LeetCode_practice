class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        isNonDecreasing = True
        for i in range(1, len(nums)):
            if nums[i] < nums[i -1]:
                isNonDecreasing = False

        if isNonDecreasing:
            return 0
        else:
            counter = 0
            while True:
                minSum = 100000
                minSumIndex = 0
                for i in range(1, len(nums)):
                    if minSum > nums[i - 1] + nums[i]:
                        minSum = nums[i - 1] + nums[i]
                        minSumIndex = i
                nums.pop(minSumIndex - 1)
                nums[minSumIndex - 1] = minSum
                print(nums)
                counter += 1
                isNonDecreasing = True
                for i in range(1, len(nums)):
                    if nums[i] < nums[i -1]:
                        isNonDecreasing = False
                if isNonDecreasing:
                    break
            
        return counter