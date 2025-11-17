class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        ans = []
        right = len(numbers) - 1
        for i, n in enumerate(numbers):
            diff = target - n
            while numbers[right] >= diff and right > i:
                if numbers[right] == diff:
                    ans.append(i + 1)
                    ans.append(right + 1)
                    return ans
                right -= 1
            # right = len(numbers) - 1
        return ans
#  O(len(numbers)) - time
# O(1) - memory