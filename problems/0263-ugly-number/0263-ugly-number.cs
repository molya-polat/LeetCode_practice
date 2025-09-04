public class Solution {
    public bool IsUgly(int n) {
        for (int k = 2; k <= 5 && n > 0; n = (n % k == 0) ? n / k : n, k += Math.Min(1, n % k));
        return n == 1;
    }
}