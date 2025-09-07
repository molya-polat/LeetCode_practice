using System;
using System.Collections.Generic;
public class Solution {
    public int GetLeastFrequentDigit(int n) {
        Dictionary<int, int> dict = new Dictionary<int, int>();
        int minAppear = n;
        int resultDigit = n;
        while(n > 0){
            int digit = n % 10;
            if (dict.ContainsKey(digit)){
                dict[digit]++;
            }
            else{
                dict.Add(digit, 1);
            }
            
            n = n / 10;
        }
        foreach (var d in dict){
            if(d.Value <= minAppear){
                resultDigit = minAppear == d.Value ? Math.Min(d.Key, resultDigit) : d.Key;
                minAppear = d.Value;
            }   
        }
       return resultDigit;
    }
}