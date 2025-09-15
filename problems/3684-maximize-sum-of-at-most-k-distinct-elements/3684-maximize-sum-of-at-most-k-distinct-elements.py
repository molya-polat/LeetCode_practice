class Solution:
    def maxKDistinct(self, nums: List[int], k: int) -> List[int]:
        resultArr = list(set(nums))
        length = min(k, len(resultArr))
        resultArr.sort(reverse=True)

        return resultArr[:length]