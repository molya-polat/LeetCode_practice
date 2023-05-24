public class Solution {
    public int RemoveElement(int[] nums, int val) {
        if (nums.Length == 0) return 0;

        int pointer1 = 0;
        int pointer2 = 0;
        while(pointer2 < nums.Length){
            if (nums[pointer2] != val){
                nums[pointer1] = nums[pointer2];
                pointer1++;
            }
            pointer2++;
        }
        return pointer1;
    }
}