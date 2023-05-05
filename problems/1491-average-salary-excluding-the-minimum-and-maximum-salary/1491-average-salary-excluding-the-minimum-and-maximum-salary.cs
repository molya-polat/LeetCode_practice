public class Solution {
    public double Average(int[] salary) {
        return (salary.Sum() - salary.Min() - salary.Max()) / (double)(salary.Length - 2);
    }
}