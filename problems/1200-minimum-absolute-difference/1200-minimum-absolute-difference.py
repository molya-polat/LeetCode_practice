class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        ans = []
        arr.sort()
        minDif = 10**9
        for i in range(len(arr) - 1):
            minDif = min(minDif, abs(arr[i] - arr[i + 1]))

        for i in range(len(arr) - 1):
            if abs(arr[i] - arr[i + 1]) == minDif:
                ans.append([arr[i], arr[i + 1]])

        return ans
        # O(n logn) - time
        # O(n^n) - space