class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        if len(fruits) < 3:
            return len(fruits)
        ct = {}
        left = 0
        right = left + 1
        max_size = 0
        ct[fruits[left]] = 1
        while right < len(fruits):
            if len(ct) < 2:
                if fruits[right] in ct:
                    ct[fruits[right]] += 1
                else:
                    ct[fruits[right]] = 1
                max_size = max(max_size, right - left + 1)
                # print("FUFFFFFF")
                # print(right)
                # print(left)
                # print(right - left + 1)
                right += 1
            else:
                if fruits[right] in ct:
                    ct[fruits[right]] += 1
                    max_size = max(max_size, right - left + 1)
                    right += 1
                else:
                    ct[fruits[left]] -= 1
                    if ct[fruits[left]] == 0:
                        ct.pop(fruits[left])
                    max_size = max(max_size, right - left)
                    # print("PPPPPPPPPPFF")
                    # print(right)
                    # print(left)
                    # print(right - left)
                    left += 1
        

        return max_size