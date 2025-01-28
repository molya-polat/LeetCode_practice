public class Solution {
    public int SubarraySum(int[] nums) {
        var result = 0;
        var length = nums.Length;
        for (int i = 0; i < length; i++){
            int start = Math.Max(0, i - nums[i]);
            int sumtemp = 0;
            for (int j = start; j <= i; j++){
                sumtemp += nums[j];
            }
            result += sumtemp;
        }

        return result;
    }
}