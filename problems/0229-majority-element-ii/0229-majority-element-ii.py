class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        result = set()
        third = len(nums) // 3
        diction = defaultdict(int)
        for n in nums:
            diction[n] += 1
            if diction[n] > third and n not in result:
                result.add(n)

        
        return list(result)

        # O(n) - time
        # O(n) - space