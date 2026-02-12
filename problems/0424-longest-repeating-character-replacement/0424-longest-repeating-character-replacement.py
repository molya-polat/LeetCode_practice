class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        start = 0
        diction = defaultdict(int)
        maxLength = 0
        maxCount = 0
        for end in range(start, len(s)):
            diction[s[end]] += 1
            maxCount = max(maxCount, diction[s[end]])

            while end - start + 1 - maxCount > k:
                diction[s[start]] -= 1
                start += 1

            maxLength = max(maxLength, end - start + 1)
        

        return maxLength

        # O(n^2) - time
        # O(n) - space