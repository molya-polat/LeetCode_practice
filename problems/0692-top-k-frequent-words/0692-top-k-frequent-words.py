class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        diction = defaultdict(int)
        for word in words:
            diction[word] += 1
        

        sorted_items = sorted(diction.items(), key=lambda x: (-x[1], x[0]))

        ans = []
        for i in range(k):
            ans.append(sorted_items[i][0])
        
        return ans

        # O(n logn) - time
        # O(n) - space