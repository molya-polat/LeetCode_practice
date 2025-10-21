class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def func(arr):
            if len(arr) == 2:
                return [[arr[0], arr[1]] , [arr[1], arr[0]]]
            elif len(arr) == 1:
                return[[arr[0]]]
            else:
                result = []
                for i in range(len(arr)):
                    funcresult = func(arr[:i] + arr[i + 1:])
                    for pair in funcresult:
                        temp = [arr[i]] + pair
                        result.append(temp)
            return result
        return func(nums)
# O(n^2) - time compl
# O(n^2) - space compl