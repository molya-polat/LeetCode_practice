class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        def merge(left, right):
            i, j, = 0, 0
            ans = [0 for _ in range(len(left) + len(right))]
            pair = False
            for m in range(len(ans)):
                if i >= len(left):
                    ans[m] = right[j]
                    j += 1
                elif j >= len(right):
                    ans[m] = left[i]
                    i += 1
                else:
                    if left[i] < right[j]:
                        ans[m] = left[i]
                        i += 1
                    else:
                        ans[m] = right[j]
                        j += 1
            if len(ans) == length:
                m = length // 2
                p, s = 0, 0
                ans1 = ans[:m]
                ans2 = ans[m:]
                if len(ans1) < len(ans2):
                    m += 1
                ans1 = ans[:m][::-1]
                ans2 = ans[m:][::-1]
                for m in range(len(ans)):
                    if s >= len(ans2):
                        ans[m] = ans1[p]
                        p += 1
                    elif p >= len(ans1):
                        ans[m] = ans2[s]
                        s += 1
                    else:
                        if m % 2 != 0:
                            ans[m] = ans2[s]
                            s += 1
                        else:
                            ans[m] = ans1[p]
                            p += 1
            
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
        ans = divide(nums)
        for i in range(len(nums)):
            nums[i] = ans[i]