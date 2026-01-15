class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = []
        st = set()
        for i in range(1, n + 1):
            st.add(i)

        for m in nums:
            if m in st:
                st.remove(m)
        return list(st)

        # O(n)- time
        # O(n) - space