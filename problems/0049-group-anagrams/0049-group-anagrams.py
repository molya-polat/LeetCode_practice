class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = []
        diction = {}
        for string in strs:
            sorted_str = "".join(sorted(string))
            if sorted_str in diction:
                diction[sorted_str].append(string)
            else:
                diction[sorted_str] = [string]
            
        for sorted_str, ls in diction.items():
            ans.append(ls)
        
        return ans

        # O(n) - time
        # O(n) - space


        
























#         ans = []
#         diction = {}
#         index = 0
#         for word in strs:
#             sortedWordCurrent = "".join(sorted(word))
#             if len(ans) == 0:
#                 ans.append([word])
#                 diction[index] = sortedWordCurrent
#                 index += 1
#             else:
#                 added = False
#                 for i, sortedWord in diction.items():
#                     if sortedWord == sortedWordCurrent:
#                         ans[i].append(word)
#                         added = True
#                         break
#                 if not added:
#                     ans.append([word])
#                     diction[index] = sortedWordCurrent
#                     index += 1
        
#         return ans
# # O(n^2) - time
# # O(n) - memory