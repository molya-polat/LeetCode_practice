public class Solution {
    public int[] PlusOne(int[] digits) {      
        // if (digits[digits.Length - 1] == 9){ // last number is 9
        //     digits[digits.Length - 1] = 0;
        //     if (digits.Length > 1){ //length should greater than 1
        //         for (int i = digits.Length - 2; i > -1; i--){
        //         if (digits[i] == 9){ // next number is 9
        //             digits[i] = 0;
        //             if (i == 0){ //first number is 9 => length + 1;
        //                 int [] result = new int [digits.Length + 1];
        //                 result[0] = 1;
        //                 for (int j = 1; j < result.Length; j++){
        //                     result[j] = digits[j - 1];
        //                 }
        //                 return result;
        //             }                    
        //         }
        //         else{// next number is not 9
        //             digits[i] = digits[i] + 1;
        //             break;
        //         }
        //         }
        //     }
        //     else{ // length is 1
        //         int [] result = new int [digits.Length + 1];
        //         result[0] = 1;
        //             for (int j = 1; j < result.Length; j++){
        //                 result[j] = digits[j - 1];
        //             }
        //         return result;
        //     }           
        // } 
        // else{// last number is not 9
        //     digits[digits.Length - 1] = digits[digits.Length - 1] + 1;
        // }
        // return digits;
          for(int i = digits.Length - 1; i >= 0; i--){
            if(digits[i] < 9){
                digits[i]++;
                return digits;
            }
            digits[i] = 0;
        }

        int[] digits2 = new int[digits.Length + 1];
        digits2[0] = 1;
        return digits2;
    }
}