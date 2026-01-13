class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        non_sorted = []
        for n in nums:
            non_sorted.append(n * n)
        
        def merge(left, right):
            result = [0 for _ in range(len(left) + len(right))]
            i, j, k = 0, 0, 0
            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    result[k] = left[i]
                    i += 1
                else:
                    result[k] = right[j]
                    j += 1
                k += 1
            while i < len(left):
                result[k] = left[i]
                i += 1
                k += 1
            
            while j < len(right):
                result[k] = right[j]
                j += 1
                k += 1

            return result

        def divide(nums):
            if len(nums) <= 1:
                return nums
            med = len(nums) // 2
            left = nums[:med]
            right = nums[med:]

            if len(left) > 1:
                left = divide(left)
            if len(right) > 1:
                right = divide(right)

            return merge(left, right)

        return divide(non_sorted)

        # O(n logn) - time
    # O(n) - memory