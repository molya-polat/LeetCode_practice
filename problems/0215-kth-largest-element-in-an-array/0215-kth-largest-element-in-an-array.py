class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def merge(left, right):
            ans = []
            i, j = 0, 0
            while i < len(left) or j < len(right):
                if i < len(left) and j < len(right):
                    if left[i] > right[j]:
                        ans.append(left[i])
                        i += 1
                    else:
                        ans.append(right[j])
                        j += 1
                elif i < len(left) and j >= len(right):
                    ans.append(left[i])
                    i += 1
                elif j < len(right) and i >= len(left):
                    ans.append(right[j])
                    j += 1
            
            return ans



        def divide(nums):
            if len(nums) < 2:
                return nums

            med = len(nums) // 2
            left = nums[:med]
            right = nums[med:]
            if len(left) > 1:
                left = divide(left)
            if len(right) > 1:
                right = divide(right)
            
            return merge(left, right)




        nums = divide(nums)
        return nums[k - 1]

        # O(n logn) - time
        # O(n logn) - space