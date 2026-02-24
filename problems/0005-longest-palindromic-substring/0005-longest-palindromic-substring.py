class Solution:
    def longestPalindrome(self, s: str) -> str:
        def check(i, j):
            left = i
            right = j - 1

            while left < right:
                if s[left] != s[right]:
                    return False

                left += 1
                right -= 1

            return True

        for length in range(len(s), 0, -1):
            for start in range(len(s) - length + 1):
                if check(start, start + length):
                    return s[start : start + length]

        return ""
        # if len(s) == 1:
        #     return s
        # n = len(s)
        # palindrome_memo = [[-1] * (n - start) for start in range(n)]

        # def findMaxPalindromeFrom(start, end):
        #     if end - start <= 1:
        #         return (start, end)

        #     key = (end - 1) * n + start
        #     if palindrome_memo[start][end - start - 1] == -1:
        #         if s[start] != s[end - 1]:
        #             start_one, end_one = findMaxPalindromeFrom(start, end - 1)
        #             start_two, end_two = findMaxPalindromeFrom(start + 1, end)
        #             if end_one - start_one > end_two - start_two:
        #                 palindrome_memo[start][end - start - 1] = (start_one, end_one)
        #                 return (start_one, end_one)
        #             palindrome_memo[start][end - start - 1] = (start_two, end_two)
        #             return (start_two, end_two)
        #         else:
        #             start_one, end_one = findMaxPalindromeFrom(start + 1, end - 1)
        #             if end_one - start_one == end - start - 2:
        #                 palindrome_memo[start][end - start - 1] = (start, end)
        #                 return (start, end)
        #             else:
        #                 start_one, end_one = findMaxPalindromeFrom(start, end - 1)
        #                 start_two, end_two = findMaxPalindromeFrom(start + 1, end)
        #                 if end_one - start_one > end_two - start_two:
        #                     palindrome_memo[start][end - start - 1] = (start_one, end_one)
        #                     return (start_one, end_one)
        #                 palindrome_memo[start][end - start - 1] = (start_two, end_two)
        #                 return (start_two, end_two)
        #     else:
        #         return palindrome_memo[start][end - start - 1]

        # start_result, end_result = findMaxPalindromeFrom(0, len(s))
        # return s[start_result:end_result]