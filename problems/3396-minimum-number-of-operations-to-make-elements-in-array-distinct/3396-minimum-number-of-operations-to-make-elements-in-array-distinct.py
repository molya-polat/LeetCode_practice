class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        operations = 0

        ct = Counter(nums)
        number_of_distint_elements = len(ct)
        
        while len(nums) > 0:
            if len(nums) == number_of_distint_elements:
                return operations

            for v in nums[:3]:
                ct[v] -= 1
                if ct[v] == 0:
                    number_of_distint_elements -= 1
            nums = nums[3:]
            operations += 1

        return operations

        # O(n) -time complexity
        # O(n) - space complexity


        # 5 2 1 5

        # ct[5] = 2