class Solution:
    def mirrorFrequency(self, s: str) -> int:
        diction = defaultdict(int)
        for ch in s:
            diction[ch] += 1
        
        def findMirror(ch):
            if ord(ch) < 97:
                return ord('9') - ord(ch) + ord('0')
            
            else:
                return ord('z') - ord(ch) + ord('a')
        ans = 0
        st = set()
        for ch in s:
            if ch not in st:
                mir_ch = chr(findMirror(ch))
                ans += abs(diction[ch] - diction[mir_ch])
                st.add(ch)
                st.add(mir_ch)
        
        
        return ans

        # O(n) - time
        # O(n) - space