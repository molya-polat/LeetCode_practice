class Solution:
    def decodeString(self, s: str) -> str:
        brackets = []
        pairs_brackets = {}
        for i,ch in enumerate(s):
            if ch == '[':
                brackets.append(("[", i))
            elif ch == ']':
                open_bracket, index_open = brackets.pop()
                pairs_brackets[index_open] = i
        
        def decode(start, end, k):
            base_str = ""
            i = start
            while i < end:
                ch = s[i]
                if ord(ch) > 47 and ord(ch) < 58:
                    number = 0
                    while ord(ch) > 47 and ord(ch) < 58:
                        number = number * 10 + int(ch)
                        i += 1
                        ch = s[i]
                    start_new = i + 1
                    new_end = pairs_brackets[i]
                    base_str += decode(start_new, new_end, number)
                    i = pairs_brackets[i]
                else:
                    base_str += ch
                i += 1

            result = ""
            for j in range(k):
                result += base_str
            
            return result

        
        return decode(0, len(s), 1)


            




























        # def is_digit(ch):
        #     return ord(ch) > 47 and ord(ch) < 58

        # def is_character(ch):
        #     return ord(ch) > 96 and ord(ch) < 123

        # start2end = {}
        # stack = []
        # for i, ch in enumerate(s):
        #     if ch == '[':
        #         stack.append(i)
        #     elif ch == ']':
        #         start = stack.pop()
        #         start2end[start] = i

        # numberStart2openingBracket = {}
        # number = -1
        # prev_is_num = False
        # for i, ch in enumerate(s):
        #     if is_digit(ch):
        #         if not prev_is_num:
        #             number = int(ch)
        #         else:
        #             number = 10 * number + int(ch)
        #     elif number != -1:
        #         numberStart2openingBracket[i - len(str(number))] = (number, i)
        #     prev_is_num = is_digit(ch)

        # def recursive_decode(st, ed):
        #     if st > ed:
        #         return ''
        #     if is_character(s[st]):
        #         return s[st] + recursive_decode(st + 1, ed)
        #     if is_digit(s[st]):
        #         k, openingBracketIndex = numberStart2openingBracket[st]
        #         closingBracketIndex = start2end[openingBracketIndex]
        #         return k * recursive_decode(openingBracketIndex + 1, closingBracketIndex - 1) + recursive_decode(closingBracketIndex + 1, ed)

        # return recursive_decode(0, len(s) - 1)