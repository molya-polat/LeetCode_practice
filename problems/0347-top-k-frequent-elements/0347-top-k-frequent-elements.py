class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        diction = defaultdict(int)
        for n in nums:
            diction[n] += 1

        result = []
        sorted_diction = sorted(diction.items(), key = lambda x:x[1], reverse = True)
        for i in range(k):
            result.append(sorted_diction[i][0])
        
        return result

        # O(n) - time
        # O(n) - space