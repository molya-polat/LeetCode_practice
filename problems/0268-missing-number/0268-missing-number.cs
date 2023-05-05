public class Solution {
    public int MissingNumber(int[] nums) {
        // int length = nums.Length;
        // Array.Sort(nums);
        // if (length == 1 && nums[length -1] != 0) return 0;
        // for (int i = 0; i < length - 1; i++){
        //     if (i == 0 && nums[i] != 0) return 0;
        //     if (nums[i + 1] - nums[i] != 1) return nums[i] + 1;
        // }

        // return nums[length - 1] + 1;
        int sum = nums.Length*(nums.Length + 1) / 2;
        int total = 0;
        for(int i = 0; i< nums.Length; i++){
            total += nums[i];
        }
        return sum - total;
    }
}