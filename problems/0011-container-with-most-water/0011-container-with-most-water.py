class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = -1
        n = len(height)
        left = 0
        right = n - 1
        while left < right:
            max_area = max(max_area, ((right - left) * min(height[left], height[right])))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return max_area
        # O(n) - time
        # O(1) - space





























        # left = 0
        # right = len(height) - 1
        # maxWater = 0
        # while left < right:
        #     water = (right - left) * min(height[left], height[right])
        #     maxWater = max(maxWater, water)
        #     if height[left] < height[right]:
        #         left += 1
        #     else:
        #         right -= 1
        
        # return maxWater
        # # O(n) - time
        # # O(1) - space