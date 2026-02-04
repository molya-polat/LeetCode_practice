class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = []
        productLeft = [1]
        productRight = [1]
        for i in range(len(nums) - 1):
            productLeft.append(productLeft[i] * nums[i])
        k = 0
        for i in range(len(nums) - 1, 0, -1):
            productRight.append(productRight[k] * nums[i])
            k += 1
        n = len(nums)
        for i in range(len(nums)):
            answer.append(productLeft[i] * productRight[n - i - 1])

        return answer

        # O(n) - time
        # O(n) - space