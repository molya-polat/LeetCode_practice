class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        dct = defaultdict(int)
        for i,n in enumerate(nums2):
            dct[n] = i
        
        for j,n in enumerate(nums1):
            for i in range(dct[n], len(nums2)):
                if nums2[i] > n:
                    ans.append(nums2[i])
                    break
            if len(ans) < j + 1:
                ans.append(-1)
        
        return ans

        # O(n^2) - time
        # O(n) - memory