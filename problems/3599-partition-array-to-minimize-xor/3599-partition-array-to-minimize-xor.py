class Solution:
    def minXor(self, nums: List[int], k: int) -> int:
        INF = 10 ** 10
        n = len(nums)
        memo = {}

        # State size = n * k
        # Each state operation = n

        def get_minimum_possible_value_of_maximum_xors(r, k):
            if (r, k) in memo:
                return memo[(r, k)]

            if r + 1 < k:
                memo[(r, k)] = INF
                return INF
            
            if k == 1:
                xor = 0
                for i in range(0, r + 1):
                    xor = xor ^ nums[i]
                memo[(r, k)] = xor
                return xor

            xor = nums[r] 
            ans = INF

            for r2 in range(r - 1, -1, -1):
                # [r2 + 1, r]
                if r2 + 1 < k - 1:
                    break
                min_possible_max_xor_of_k_minus_1_subarrays = get_minimum_possible_value_of_maximum_xors(r2, k - 1)
                ans_of_cur_r2_splitting = max(min_possible_max_xor_of_k_minus_1_subarrays, xor)
                ans = min(ans, ans_of_cur_r2_splitting)
                xor = xor ^ nums[r2]

            memo[(r, k)] = ans
            return ans


        return get_minimum_possible_value_of_maximum_xors(n - 1, k)


        # O(n ^ 2 * k) - time  complexity
        # O(n * k) - space complexity