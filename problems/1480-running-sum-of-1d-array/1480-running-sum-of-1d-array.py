class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sm_result = []
        sm = 0
        for n in nums:
            sm += n
            sm_result.append(sm)

        return sm_result

        # O(n) - time
        # O(n) - space