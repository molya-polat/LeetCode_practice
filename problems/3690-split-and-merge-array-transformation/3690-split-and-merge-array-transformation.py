from collections import deque

class Solution:
    def minSplitMerge(self, nums1: List[int], nums2: List[int]) -> int:
        def hash(arr):
            return str(arr)

        visited = set()

        def neighbours_arr(arr):
            nbs = []
            for l in range(len(arr)):
                for r in range(l, len(arr)):
                    remaining_arr = arr[:l] + arr[r + 1:]
                    removed_arr = arr[l:r + 1]

                    for i in range(len(remaining_arr) + 1):
                        new_arr = remaining_arr[:i] + removed_arr + remaining_arr[i:]
                        nbs.append(new_arr)
            return nbs

        q = deque()
        q.append((nums1, 0))
        visited.add(hash(nums1))

        while q:
            cur_node, dist = q.popleft()
            if cur_node == nums2:
                return dist

            for nb in neighbours_arr(cur_node):
                if hash(nb) not in visited:
                    visited.add(hash(nb))
                    q.append((nb, dist + 1))

        return -1