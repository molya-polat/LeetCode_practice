class Solution:
    def maximizeExpressionOfThree(self, nums: List[int]) -> int:

        def merge(left, right):
            ans = [0 for _ in range(len(left)+len(right))]
            l, r = 0, 0
            for i in range(len(ans)):
                if l >= len(left) and r < len(right):
                    ans[i] = right[r]
                    r += 1
                elif r >= len(right) and l < len(left):
                    ans[i] = left[l]
                    l += 1
                elif l < len(left) and r < len(right):
                    if left[l] <= right[r]:
                        ans[i] = left[l]
                        l += 1
                    else:
                        ans[i] = right[r]
                        r += 1
            return ans


        def divide(nums):
            m = len(nums) // 2
            left = nums[:m]
            right = nums[m:]
            if len(left) > 1:
                left = divide(left)
            if len(right) > 1:
                right = divide(right)
            
            return merge(left, right)
        
        sn = divide(nums)
        return sn[len(sn) - 1] + sn[len(sn) - 2] - sn[0]

        # O(nlogn) - time
        # O(nlogn) - memory