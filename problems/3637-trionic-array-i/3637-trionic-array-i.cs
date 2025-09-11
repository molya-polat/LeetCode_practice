public class Solution {
    public bool IsTrionic(int[] nums) {
        int p = 0;
        int q = 0;
        int k = 0;
        for (int i = 1; i < nums.Length; i++){
            if(nums[i - 1] == nums[i]){
                return false;
            }
            else if(p == 0 && nums[i - 1] > nums[i]) 
                return false;
            else if(q == 0 && nums[i - 1] < nums[i]){
                p = i;
            }
            else if(p != 0 && k == 0 && nums[i - 1] > nums[i]){
                q = i;
            }
            else if(p!= 0 && q != 0 && nums[i - 1] < nums[i]){
                k = i;
            }
            else if(p != 0 && q != 0 && nums[i -1] > nums[i]){
                return false;
            }
        }
        Console.WriteLine(p + " "+ q + " " + k);
        if(k == nums.Length - 1) return true;
        return false;
    }
}