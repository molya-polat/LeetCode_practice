class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        diction = defaultdict(int)
        for i, n in enumerate(nums):
            if n in diction:
                if i - diction[n] <= k:
                    return True
            diction[n] = i
        
        return False