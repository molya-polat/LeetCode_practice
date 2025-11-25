class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        ans = set()
        nums = sorted(nums)

        for u, a in enumerate(nums):

            i = u + 1
            j = len(nums) - 1

            while i < j:
                
                if nums[i] + nums[j] + a == 0:
                    ans.add((a, nums[i], nums[j]))

                    i += 1
                    j -= 1
                
                elif nums[i] + nums[j] + a > 0:
                    j -= 1
                
                elif nums[i] + nums[j] + a < 0:
                    i += 1

                
        return [list(t) for t in ans]

        # O(n^2) time complexity
        # O(n^2) space complexity