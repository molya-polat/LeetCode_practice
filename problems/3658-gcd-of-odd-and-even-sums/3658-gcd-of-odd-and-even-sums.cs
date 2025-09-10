public class Solution {
    public int gcd(int a, int b) {
        if (b == 0)
            return a;
        return gcd(b, a % b);
    }
    public int GcdOfOddEvenSums(int n) {
        int sumOdd = n * n;
        int sumEven = n * n + n;

        int mx = sumEven;
        int mn = sumOdd;
        // O(log n)
        return gcd(mx, mn);
    }
}