class Solution:
    def canJump(self, nums: List[int]) -> bool:
        length = len(nums)
        checked_state = set()

        def collect_or_can_reach(index):
            if index not in checked_state:
                checked_state.add(index)

                if nums[index] == 0 and index != length - 1:
                    return False

                if nums[0] >= index:
                    return True

                these_indices_can_reach_end = []
                for i in range(index - 1, 0, -1):
                    if i + nums[i] >= index:
                        if collect_or_can_reach(i):
                            return True
                    
                return False 
            return False

        return collect_or_can_reach(length - 1)

    #   memory O(n)
    # time O(n)