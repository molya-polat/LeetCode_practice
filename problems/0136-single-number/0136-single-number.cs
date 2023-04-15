public class Solution {
    public int SingleNumber(int[] nums) {
        // var hashtable = new Dictionary<int, int>();
        // for (int i = 0; i < nums.Length; i++){
        //     if (hashtable.ContainsKey(nums[i])){
        //         hashtable[nums[i]]++;
        //     }
        //     else{
        //          hashtable.Add(nums[i], 1);
        //     }           
        // }
        // foreach(var value in hashtable){
        //     if(value.Value == 1){
        //         return value.Key;
        //     }
        // }
        // return -1;
          if(nums.Length == 1)
            return nums[0];
        Array.Sort(nums);
        //1 1 2 2 4
        for(int i = 0; i < nums.Length; i = i+2)
        {
            if(i+1 < nums.Length && nums[i]!=nums[i+1])
            {
                return nums[i];
            }
            else if(i+1 == nums.Length  && nums[i]!=nums[i-1])
            {                
                    return nums[i];
            }          
        }
        return 0;
    }
}