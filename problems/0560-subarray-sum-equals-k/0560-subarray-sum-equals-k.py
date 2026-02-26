class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        diction = defaultdict(int)
        sm = 0
        count = 0
        for i,n in enumerate(nums):
            sm += n
            if sm - k in diction:
                count += diction[sm - k]
            if sm == k:
                count += 1
            
            diction[sm] += 1
        
        return count









        
        # diction = {}
        # sm = 0
        # result = 0
        # for i, n in enumerate(nums):
        #     sm += n
        #     if sm - k in diction:
        #         result += len(diction[sm - k])
        #     if sm in diction:
        #         diction[sm].append(i)
        #     else:
        #         diction[sm] = [i]
        #     if sm == k:
        #         result += 1
            
        # return result

        # # O(n) - time
        # # O(n) - space