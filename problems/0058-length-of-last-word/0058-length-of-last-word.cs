public class Solution {
    public int LengthOfLastWord(string s) {
        var arr = s.Trim().Split(" ");
        return arr[arr.Length - 1].Length;
    }
}