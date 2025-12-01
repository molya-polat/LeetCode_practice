class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        prefix_digit_sum = [0]
        for c in s:
            last_sum = prefix_digit_sum[-1]
            prefix_digit_sum.append(last_sum + int(c))

        def digit_sum(l, r):
            return prefix_digit_sum[r + 1] - prefix_digit_sum[l]

        MOD = 10 ** 9 + 7
        prefix_k = [0]
        number_of_digits = [0]
        for c in s:
            last_k = prefix_k[-1]
            last_pw = number_of_digits[-1]
            if c == '0':
                prefix_k.append(last_k)
                number_of_digits.append(last_pw)
            else:
                new_k = (last_k * 10 + int(c)) % MOD
                prefix_k.append(new_k)
                number_of_digits.append(last_pw + 1)

        powers_of_10_mod = [1]
        for pw in range(1, 10 ** 5 + 1):
            last_pw_10 = powers_of_10_mod[-1]
            new_pw_10 = (last_pw_10 * 10) % MOD
            powers_of_10_mod.append(new_pw_10)


        def find_k_mod(l, r):
            d = number_of_digits[r + 1] - number_of_digits[l]
            pw_10_d = powers_of_10_mod[d] 

            k = prefix_k[r + 1] - pw_10_d * prefix_k[l]

            return k % MOD

        ans = []
        for l, r in queries:
            a = find_k_mod(l, r) * digit_sum(l, r) % MOD
            ans.append(a)

        return ans

        # O(len(s) + len(queries)) - time complexity
        # O(len(s) + len(queries)) - memory complexity

        # 10203004
        # l = 2, r = 4

        # prefix_k[5] = 123
        # prefix_k[2] = 1

        # prefix_k[5] - 10 ^ d * prefix_k[2] = 23

        # prefix_k[0] = 0
        # 1 -> 1
        # 2 -> 10
        # 3 -> 102
        # 4 -> 1020
        # 5 -> 10203