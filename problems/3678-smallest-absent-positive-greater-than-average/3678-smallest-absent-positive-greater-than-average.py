class Solution:
    def smallestAbsent(self, nums: List[int]) -> int:
        average : double = sum(nums) / len(nums)
        average = 0 if average <= 0 else average
        while True:
            if int(average + 1) not in nums:
                return int(average + 1)
            else:
                average += 1

        return 1