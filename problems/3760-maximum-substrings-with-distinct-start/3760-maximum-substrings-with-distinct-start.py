class Solution:
    def maxDistinct(self, s: str) -> int:
        st = set()
        counter = 0
        for ch in s:
            if ch not in st:
                counter += 1
                st.add(ch)
        
        return counter

        # O(len(s)) - time
        # O(len(s)) - memory