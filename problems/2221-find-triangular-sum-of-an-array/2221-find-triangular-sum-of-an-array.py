class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        triangularSum = nums[0]
        while len(nums) > 1:
            newNum = []
            for i in range(len(nums) - 1):
                newNum.append((nums[i] + nums[i+1]) % 10)
            
            nums = newNum
            triangularSum = nums[0]

        return triangularSum
        # O(n^2) - time compl
        # O(n) - space compl