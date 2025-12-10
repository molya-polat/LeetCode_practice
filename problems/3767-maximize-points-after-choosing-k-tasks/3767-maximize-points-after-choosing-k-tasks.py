class Solution:
    def maxPoints(self, technique1: List[int], technique2: List[int], k: int) -> int:
        max_points = - 10 ** 9
        max_sum = 0
        curr_k = 0
        unchosen1 = []
        for i in range(len(technique1)):
            if technique1[i] >= technique2[i]:
                max_sum += technique1[i]
                curr_k += 1
            else:
                unchosen1.append(i)
                max_sum += technique2[i]
        
        if curr_k >= k:
            return max_sum
        
        diff = k - curr_k
        diff_arr = []
        for index in unchosen1:
            diff_arr.append(technique2[index] - technique1[index])
        diff_arr_sorted = sorted(diff_arr)
        diff_arr_sorted = diff_arr_sorted[:diff]
        return max_sum - sum(diff_arr_sorted)

        # O(n) - time
        # O(n) - memory