class Solution:
    def buttonWithLongestTime(self, events: List[List[int]]) -> int:
        buttonLong = events[0][0]
        longtime = events[0][1]
        previousTime = 0
        for time in events:
            if longtime < time[1] - previousTime:
                longtime = time[1] - previousTime
                buttonLong = time[0]
            elif longtime == time[1] - previousTime:
                buttonLong = min(buttonLong, time[0])
            previousTime = time[1]
            
        
        return buttonLong

        # O(n) - time compl
        # O(1) - space compl