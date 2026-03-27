class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positive = []
        negative = []
        for n in nums:
            if n < 0:
                negative.append(n)
            else:
                positive.append(n)
        ans = []
        for i in range(len(positive)):
            ans.append(positive[i])
            ans.append(negative[i])
        
        return ans

        # O(N) - time
        # O(n) - space