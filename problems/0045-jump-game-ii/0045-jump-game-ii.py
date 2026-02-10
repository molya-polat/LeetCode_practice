class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0
        if n == 2:
            if nums[0] == 0:
                return -1
            else:
                return 1
                
        minJumps = [10**7 for _ in range(n)]
        minJumps[n - 1] = 10**7
        minJumps[n - 2] = 1
        if nums[n - 2] == 0:
            minJumps[n - 2] = 10**7
        for i in range(n - 3, -1, -1):
            if nums[i] > 0:
                if nums[i] >= n - 1 - i:
                    minJumps[i] = 1
                elif nums[i] < n - 1 - i:
                    minFrom = min(minJumps[i + 1:i + nums[i] + 1])
                    minJumps[i] = 1 + minFrom
        if minJumps[0] >= 10**7:
            return -1
        
        return minJumps[0]

        # O(n) - time
        # O(n) - memory