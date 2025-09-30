class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        # diction = defaultdict(int)
        # for i in range(0, len(nums) - k + 1):
        #     setSubArray = set()
        #     for j in range(i, i + k):
        #         if nums[j] not in setSubArray:
        #             diction[nums[j]] += 1
        #             setSubArray.add(nums[j])

        # for number, arrays in sorted(diction.items())[::-1]:
        #     if arrays == 1:
        #         return number
        # return -1

        diction = defaultdict(int)
        for i in range(0, len(nums) - k + 1):
            for a in set(nums[i:i+k]):
                diction[a] += 1

        for number, arrays in sorted(diction.items())[::-1]:
            if arrays == 1:
                return number
        return -1