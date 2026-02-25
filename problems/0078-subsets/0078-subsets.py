class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]

        def subsetsFrom(numbers, k):
            if not numbers:
                return None

            ans = []
            if k == 1:
                for n in numbers:
                    ans.append([n])
                return ans
            for i in range(len(numbers)):
                current_main = numbers[i]
                others = numbers[i + 1:]
                sets = subsetsFrom(others, k - 1)
                if sets:
                    for st in sets:
                        if st:
                            st.append(current_main)
                            ans.append(st)
            return ans
        
        for i in range(1, len(nums) + 1):
            i_set = subsetsFrom(nums, i)
            result.extend(i_set)
        
        return result

        # O(n^2) - time
        # O(n^2) - space