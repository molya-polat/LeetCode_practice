class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        max_sum = - 10 ** 9
        diction = {}

        def function(i_start):
            if i_start in diction:
                return diction[i_start]
            if i_start == len(arr):
                diction[i_start] = 0
                return 0
                
            max_sum = - 10 ** 9
            for p in range(1, k + 1):
                if i_start + p >= len(arr):
                    sm_left_part = max(arr[i_start:]) * len(arr[i_start:])
                    max_sum = max(max_sum, sm_left_part) 
                else:
                    sm_left_part = max(arr[i_start:i_start + p]) * p
                    max_sum = max(max_sum, sm_left_part + function(p + i_start))
            diction[i_start] = max_sum
            return max_sum
        
        return function(0)

        # O(len(arr)^3) - time
        # O(len(arr)) - memory