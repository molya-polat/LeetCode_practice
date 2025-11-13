class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        temp = nums1.copy()
        j = 0
        k = 0
        for i in range(m + n):
            if j >= n:
                nums1[i] = temp[k]
                k += 1
            else:
                if k < m and temp[k] < nums2[j]:
                    nums1[i] = temp[k]
                    k += 1
                else:
                    nums1[i] = nums2[j]
                    j += 1
            

            # O(m+n) = O(m + n) - time, memory