public class Solution {
    public int EarliestFinishTime(int[] landStartTime, int[] landDuration, int[] waterStartTime, int[] waterDuration) {
        int earliestTime = int.MaxValue;
        int firstEndTime = 0;
        int secondEndTime = 0;
        for (int i = 0; i < landStartTime.Length; i++){  
            for(int j = 0; j < waterStartTime.Length; j++){
                firstEndTime = landStartTime[i] + landDuration[i];
                secondEndTime = firstEndTime > waterStartTime[j] ? firstEndTime + waterDuration[j] : waterStartTime[j] + waterDuration[j];

                earliestTime = Math.Min(earliestTime, secondEndTime); //update new time
                firstEndTime = waterStartTime[j] + waterDuration[j]; //vice versa
                secondEndTime = firstEndTime > landStartTime[i] ? firstEndTime + landDuration[i] : landStartTime[i] + landDuration[i];

                earliestTime = Math.Min(earliestTime, secondEndTime); //update new time
            }
        }

        return earliestTime;
    }
}