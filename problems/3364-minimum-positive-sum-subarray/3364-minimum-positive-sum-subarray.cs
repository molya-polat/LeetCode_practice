public class Solution {
    public int MinimumSumSubarray(IList<int> nums, int l, int r) {
        int minSum = 2000000;
        int n = nums.Count();

        for (int i = 0; i < n; i++) {
            int sum = 0;
            
            for (int m = i; m < i + l - 1; m++){
                if(m >= n) break;
                sum += nums[m];
            }
            for (int s = i + l - 1; s <= i + r - 1; s++) {
                if(s >= n) break;
                sum += nums[s];
                if(sum > 0) {
                    minSum = Math.Min(minSum, sum);
                }
            }
            
        }
        return minSum == 2000000 ? -1 : minSum;
    }
}