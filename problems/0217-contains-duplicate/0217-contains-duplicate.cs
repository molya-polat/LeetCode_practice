public class Solution {
    public bool ContainsDuplicate(int[] nums) {
        // var dict = new Dictionary<int, int>();
        // for (int i = 0; i < nums.Length; i++){
        //     if (!dict.ContainsKey(nums[i])){
        //         dict.Add(nums[i], 1);
        //     }
        //     else{
        //         dict[nums[i]]++;
        //     }
        // }
        // foreach (var d in dict){
        //     if (d.Value > 1) return true;
        // }
        // return false;
        var uniqueNums = new HashSet<int>(nums);

        if(uniqueNums.Count < nums.Length)
            return true;
        else
            return false;
    }
}