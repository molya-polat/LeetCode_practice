class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort() #should I implement it by myself
        counter = 0 
        minEl = nums[0]
        for i in range(1, len(nums)):
            if nums[i] - minEl > k:
                counter += 1
                minEl = nums[i]
        counter += 1
        return counter

        # O(n) - time compl
        # O(n) - space compl