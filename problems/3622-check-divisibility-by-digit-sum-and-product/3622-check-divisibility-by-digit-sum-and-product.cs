public class Solution {
    public bool CheckDivisibility(int n) {
        int initialNumber = n;
        int sumOfDigits = 0;
        int productOfDigits = 1;
        int digit = 0;
        while(n > 0){
            digit = n % 10;
            sumOfDigits += digit;
            productOfDigits *= digit;
            n = n / 10;
        }
        return (initialNumber % (sumOfDigits + productOfDigits)) == 0;
    }
}