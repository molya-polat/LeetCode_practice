class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        ans = []
        diction = {}
        for i, ch in enumerate(s):
            if ch not in diction:
                diction[ch] = (i, i)
            else:
                prev_start, prev_end = diction[ch]
                diction[ch] = (prev_start, i)
        
        intervals = diction.values()
        sorted_intervals = sorted(intervals, key = lambda x: x[0])
        current_start, current_end = -1, -1
        for start, end in sorted_intervals:
            if current_start == -1 and current_end == -1:
                current_start = start
                current_end = end
            else:
                if start > current_end and start > current_start:
                    ans.append(current_end - current_start + 1)
                    current_start = start
                    current_end = end
                else:
                    if start < current_start:
                        current_start = start

                    if end > current_end:
                        current_end = end
        
        ans.append(current_end - current_start + 1)
        
        return ans

        # O(n) - time
        # O(n) - space