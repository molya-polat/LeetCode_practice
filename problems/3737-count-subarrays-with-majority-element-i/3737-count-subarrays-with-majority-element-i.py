class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        pre_occur = [0 for _ in range(len(nums))]
        cur_target = 0
        for i, n in enumerate(nums):
            if n == target:
                cur_target += 1
            
            pre_occur[i] = cur_target
        subarr = cur_target
        for i in range(0, len(nums)):
            for j in range(i + 1, len(nums)):
                length = j - i + 1
                if i != 0 and length // 2 < pre_occur[j] - pre_occur[i - 1]:
                    subarr += 1
                elif i == 0 and length // 2 < pre_occur[j]:
                    subarr += 1

        
        return subarr

        # O(n^2) - time
        # O(n) - memory