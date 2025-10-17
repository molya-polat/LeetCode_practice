class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        result = [0 for _ in range(len(nums))]
        length = len(nums)
        for i in range(length):
            newIndex = i
            steps = abs(nums[i]) % length
            if nums[i] > 0:
                if i + steps >= length:
                    newIndex = (i + steps) % length
                else:
                    newIndex = i + steps
            elif nums[i] < 0:
                if i - steps < 0:
                    newIndex = length + (i - steps)
                else:
                    newIndex = i - steps
            result[i] = nums[newIndex]

        return result

        # O(n) - time compl
        # O(n) - space compl