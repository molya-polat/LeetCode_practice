class Solution:
    def minArraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        INF = sum(nums)

        dp = [INF for _ in range(n)]

        prefix = []
        sm = 0
        for a in nums:
            sm += a
            prefix.append(sm)

        rem2index = {}

        for i in range(n):
            if i > 0:
                dp[i] = min(dp[i], nums[i] + dp[i - 1])
            else:
                dp[i] = min(dp[i], nums[i])

            rem = prefix[i] % k
            if rem == 0:
                dp[i] = 0
            if rem in rem2index:
                j = rem2index[rem]
                dp[i] = min(dp[i], dp[j])
            
            rem2index[rem] = i

        return dp[n - 1]
            

        # O(n) - time   complexity
        # O(n) - memory complexity