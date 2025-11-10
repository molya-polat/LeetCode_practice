class Solution:
    def countStableSubarrays(self, capacity: List[int]) -> int:
        counter = 0
        diction = {}
        dictionSum = defaultdict(int)
        sm = 0
        for i, c in enumerate(capacity):
            sm += c
            dictionSum[i] += sm
            if c in diction:
                diction[c].append(i)
            else:
                diction[c] = [i]

        for n, tupl in diction.items():
            d = defaultdict(int)
            for index in tupl:
                otherSum = dictionSum[index] - 2 * n
                if otherSum in d:
                    counter += d[otherSum]
                d[dictionSum[index]] += 1
        prev = capacity[0]

        for i in range(1, len(capacity)):
            if prev == capacity[i] and prev == 0:
                counter -= 1
            prev = capacity[i]


        return counter
        # O(n) - time
        # O(n) - memory