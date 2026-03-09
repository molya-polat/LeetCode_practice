class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if k == 0:
            return num
        removes = 0

        stack = []
        for i in range(len(num)):
            digit = int(num[i])
            while stack and stack[-1] > digit and removes < k:
                removes += 1
                stack.pop()
            stack.append(digit)
        
        while removes < k:
            stack.pop()
            removes += 1
            
        ans = ""
        for i,digit in enumerate(stack):
            if ans == "" and digit == 0:
                continue
            ans += str(digit)

        if ans == "":
            ans = "0"
        return ans





























        if k == 0:
            return num
        # i = 0
        # while i < k:
        #     digits = list(num)
        #     prev_digit, index = 0, len(num) - 1
        #     for l,d in enumerate(digits):
        #         if prev_digit > int(d):
        #             index = l - 1
        #             break
        #         else:
        #             prev_digit = int(d)
        #     num = num[:index] + num[index + 1:]
        #     if not num:
        #         return "0"

        #     j = 0
        #     while j < len(num) and num[j] == '0':
        #         j += 1
        #     num = num[j:]
        #     i += 1
        # if num == "":
        #     num = "0"
        # return num