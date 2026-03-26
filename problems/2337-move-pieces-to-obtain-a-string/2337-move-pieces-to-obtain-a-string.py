class Solution:
    def canChange(self, start: str, target: str) -> bool:
        count_L = 0
        count_R = 0
        order1 = []
        d1 = {'L': [], 'R': []}
        for i,ch in enumerate(start):
            if ch == 'L':
                count_L += 1
                d1[ch].append(i)
                order1.append(ch)
            if ch == 'R':
                count_R += 1
                d1[ch].append(i)
                order1.append(ch)
        count_L_target = 0
        count_R_target = 0
        order2 = []
        d2 = {'L': [], 'R': []}
        for i,ch in enumerate(target):
            if ch == 'L':
                count_L_target += 1
                d2[ch].append(i)
                order2.append(ch)
            if ch == 'R':
                count_R_target += 1
                d2[ch].append(i)
                order2.append(ch)
        
        if count_L != count_L_target or count_R != count_R_target or order1 != order2:
            return False
        
        l1_values = d1['L']
        l2_values = d2['L']
        for i in range(count_L):
            if l1_values[i] < l2_values[i]:
                return False
        r1_values = d1['R']
        r2_values = d2['R']
        for i in range(count_R):
            if r1_values[i] > r2_values[i]:
                return False
        
        return True

        # O(n) - time
        # O(n) - space