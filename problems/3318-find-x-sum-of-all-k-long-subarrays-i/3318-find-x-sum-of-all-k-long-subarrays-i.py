class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        result = []
        for i in range(len(nums) - k + 1):
            sm = 0
            diction = defaultdict(int)
            for j in range(i, i + k):
                diction[nums[j]] += 1
            counter = 0
            values = sorted(diction.values(), reverse=True)[:x]
            for num, freq in sorted(diction.items(), reverse=True):
                i = 0
                while len(values) > 0 and i < len(values):
                    if values[i] == freq:
                        sm += num * freq
                        values = values[:i] + values[i + 1:]
                        break
                    else:
                        i += 1
                    
            result.append(sm) 
        return result  
# O(n^2) - time compl
# O(n) - space compl