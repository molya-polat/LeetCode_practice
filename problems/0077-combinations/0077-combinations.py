class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        all_nums = [i for i in range(1, n + 1)]

        def func(nums, p):
            if p == 0:
                return [[]]
            elif len(nums) == p:
                return [list(nums)]

            A = nums[len(nums) - 1]

            # We will take A
            result = func(nums[:len(nums) - 1], p - 1)
            for arr in result:
                arr.append(A)

            # We will not take A
            result2 = func(nums[:len(nums) - 1], p)

            
            return result + result2

            
        ans = func(all_nums, k)

        return ans
        # O(C(n,k) * k) - time and memory