class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        setNums = set(nums)


        def rec2(k, mask):
            if mask in memo:
                return memo[mask]
            if mask in setNums:
                return mask * k

            mx = ans[0]
            for d in range(20):
                if mask & (1 << d) != 0:
                    next_mask = mask ^ (1 << d)

                    if k * next_mask > mx:
                        a = rec2(k, next_mask)
                        mx = max(mx, a)
            
            memo[mask] = mx
            return mx
            

        def maxProductFor(k):
            opp_k = 0
            for d in range(20):
                pw_d = 1 << d
                if (k > pw_d) and ((k & pw_d) == 0):
                    opp_k += pw_d

            if k * opp_k > ans[0]:
                return rec2(k, opp_k)
            return 0
        
        memo = {}
        ans = [0]
        sl = sorted(setNums, reverse = True)
        for k in sl:
            a = maxProductFor(k)
            ans[0] = max(ans[0], a)

        return ans[0]