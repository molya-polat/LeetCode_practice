class Solution:
    def numDecodings(self, s: str) -> int:
        mapping = set()
        memo = {}
        for i in range(1, 27):
            mapping.add(str(i))
        
        def decode_ways(string):
            if not string:
                return 0
            if string[0] == '0':
                return 0
            if len(string) == 1:
                return 1
            if len(string) == 2:
                if string in mapping:
                    if '0' not in string:
                        return 2
                    return 1
                else:
                    if '0' not in string:
                        return 1
                    return 0
            if string not in memo:

                ways1 = decode_ways(string[1:])
                ways2 = 0
                if string[0:2] in mapping:
                    ways2 += decode_ways(string[2:])
                memo[string] = ways1 + ways2
            return memo[string]
        
        return decode_ways(s)

        # O(n) - time
        # O(n) - space