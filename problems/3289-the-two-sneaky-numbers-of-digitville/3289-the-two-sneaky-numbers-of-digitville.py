class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        sneakyNums = []
        diction = defaultdict(int)
        for n in nums:
            diction[n] +=1
            if diction[n] == 2:
                sneakyNums.append(n)
                if len(sneakyNums) == 2:
                    return sneakyNums
        return sneakyNums
        # O(n) - time
        # O(n) - mem