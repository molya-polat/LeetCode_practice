class Solution:
    def minimumDeletions(self, s: str) -> int:
        memo = {}
        a_list = [0 for _ in range(len(s) + 1)]
        a_counter = 0
        for i,ch in enumerate(s):
            if ch == 'a':
                a_counter += 1
            a_list[i + 1] = a_counter
            
        def minDel(start, end):
            if (start, end) not in memo:
                if end - start == 1:
                    memo[(start, end)] = 0
                    return 0
                # Delete first 'b'
                k = -1
                for i in range(start + 1, end):
                    if s[i] == 'b':
                        k = i
                        break
                result_one = 1
                if k >= 0:
                    result_one += minDel(k, end)
                
                # Keep first b
                result_two = a_list[end] - a_list[start]
                memo[(start, end)] = min(result_one, result_two)
            return memo[(start, end)]


        start = -1
        for i, ch in enumerate(s):
            if ch == 'b':
                start = i
                break
        if start == -1:
            return 0
        return minDel(start, len(s))


# O(n) - time
# O(n) - space