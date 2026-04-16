from sortedcontainers import SortedList


class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        N       = len(nums)
        MOD     = (10 ** 9 + 7)
        dp      = [1 for _ in range(N + 1)]
        sufx_dp = [0 for _ in range(N + 2)]
        sufx_dp[N]     = 1
        sufx_dp[N - 1] = 2

        T = {'t0': N}
        sl = SortedList()
        sl.add(nums[N - 1])

        def find_t0_optimized(start):
            sl.add(nums[start])
            t1 = T['t0']

            while sl[-1] - sl[0] > k:
                sl.remove(nums[t1 - 1])
                t1 -= 1
            
            T['t0'] = t1


        for start in range(N - 2, -1, -1): # Linear 
            find_t0_optimized(start) # logarithm 

            partitions = sufx_dp[start + 1] - sufx_dp[T['t0'] + 1]
            dp[start] = partitions % MOD
            sufx_dp[start] = (sufx_dp[start + 1] + dp[start]) % MOD

        return dp[0] % MOD

        # Time complexity   O(n logn)
        # Space complexity  O(n)