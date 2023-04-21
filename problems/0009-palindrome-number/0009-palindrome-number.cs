public class Solution {
    public bool IsPalindrome(int x) {
        // var charArr = x.ToString().ToCharArray();
        // int length = charArr.Length;       
        //     if (length > 2){
        //         for (int i = 0; i < length / 2 ; i++){
        //             if (charArr[i] != charArr[length - i - 1]){
        //                 return false;
        //             }
        //         }
        //     }
        //     else if (length == 2){
        //         if (charArr[0] != charArr[1]){
        //             return false;
        //         }
        //     }   
        // return true;
        int r = 0, c = x;
        while (c > 0)
        {
            r = r * 10 + c % 10;
            c /= 10;
        }
        return r == x; 
    }
}