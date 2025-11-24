class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        M = len(matrix)
        N = len(matrix[0])

        def access(i):
            return matrix[i // N][i % N]

        def searchInRow():
            start = 0
            end = N * M
            mid = (start + end) // 2
            while mid > - 1 and mid < N * M and start < end:
                if target == access(mid):
                    return True
                elif target < access(mid):
                    end = mid
                else:
                    start = mid + 1
                mid = (start + end) // 2
            
            return False

        return searchInRow()
        # O(log(m*n)) - time
        # O(1) - memory