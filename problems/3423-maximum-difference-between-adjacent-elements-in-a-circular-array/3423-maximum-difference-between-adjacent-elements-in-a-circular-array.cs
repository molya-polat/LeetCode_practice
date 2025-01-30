public class Solution {
    public int MaxAdjacentDistance(int[] nums) {
        int n = nums.Length;
        int maxDiff = Math.Abs(nums[0] -  nums[n - 1]);
        int diff;
        for (int i = 0; i < n - 1; i++) {
            diff = Math.Abs(nums[i] - nums[i + 1]);
            maxDiff = Math.Max(maxDiff, diff);
        }
        
        return maxDiff;
    }
}