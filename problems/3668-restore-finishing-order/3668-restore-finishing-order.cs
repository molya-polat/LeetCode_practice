using System;
public class Solution {
    public int[] RecoverOrder(int[] order, int[] friends) {
        int [] resultArray = new int[friends.Length];
        int indexFinal = 0;
        for (int i = 0; i < order.Length; i++){
            int index = Array.IndexOf(friends, order[i]);
            if(index >= 0){
                resultArray[indexFinal] = order[i];
                indexFinal++;
            }
        }

        return resultArray;
    }
}