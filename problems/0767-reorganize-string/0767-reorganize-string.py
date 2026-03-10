class Solution:
    def reorganizeString(self, s: str) -> str:
        diction = defaultdict(int)
        for ch in s:
            diction[ch] += 1

        def pop_max_not_equal(last_char):
            mx_ch, mx_ct = '', -1
            for ch, ct in diction.items():
                if ch != last_char and mx_ct < ct and ct > 0:
                    mx_ch, mx_ct = ch, ct

            diction[mx_ch] -= 1
            return mx_ch
        
        last_char = ''
        return_str = ''
        for _ in range(len(s)):
            new_char = pop_max_not_equal(last_char)
            if new_char == '':
                return ''

            return_str += new_char
            last_char = new_char

        return return_str
                



        # diction = defaultdict(int)
        # for ch in s:
        #     diction[ch] += 1
        
        # number2letters = {}
        # for letter, number in diction.items():
        #     if number not in number2letters:
        #         number2letters[number] = []
        #     number2letters.append(letter)
        
        # answer = ""
        # special = []
        # for number, letters in number2letters:
        #     temp = "".join(letters)
        #     if len(letters) != 1:
        #         while number > 1:
        #             temp += temp
        #             number -= 1
        #         answer += temp
        #     else:
        #         heapq.heappush(special, (number, letters[0]))
        #         # special.append((number, letters[0]))
        # print(special)
        # while True:
        #     number, letter = heapq.heappop(special)
        #     temp = ''
        #     if special:
        #         for n, ch in special:
        #             temp += ch
        #             special.remove(n, ch)
        #             heapq.heapify(special)
        #             heapq.heappush(special, (n - number, ch))
        #             while number > 1:
        #                 temp += temp
        #                 number -= 1
        #             answer += temp
        #     else: