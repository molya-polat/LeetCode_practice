class Solution:
    def intToRoman(self, num: int) -> str:
        diction = {}
        diction[1] = 'I'
        diction[5] = 'V'
        diction[10] = 'X'
        diction[50] = 'L'
        diction[100] = 'C'
        diction[500] = 'D'
        diction[1000] = 'M'
        diction[4] = 'IV'
        diction[40] = 'XL'
        diction[400] = 'CD'
        diction[9] = 'IX'
        diction[90] = 'XC'
        diction[900] = 'CM'

        ans = ''
        power_ten = 0
        while num > 0:
            n = num % 10
            if n < 4:
                ans = n * diction[10**power_ten] + ans
            elif n == 4:
                ans = diction[4 * 10**power_ten] + ans
            elif n > 4 and n < 9:
                ans = diction[5 * 10**power_ten] + (n - 5) * diction[10**power_ten] + ans
            elif n == 9:
                ans = diction[9 * 10**power_ten] + ans
            power_ten += 1
            num = num // 10
        
        return ans

        # O(log n) - time
        # O(1) - memory