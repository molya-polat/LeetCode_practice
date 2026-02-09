class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        st = set(wordDict)
        memo = {}
        def presentInDict(string):
            if string in st:
                return True
            else:
                return False
        
        def checkString(string):
            if string in memo:
                return memo[string]
            else:
                if len(string) == 1:
                    memo[string] = presentInDict(string)
                    return memo[string]
                else:
                    for i in range(len(string)):
                        if presentInDict(string[:i + 1]):
                            if i == len(string) - 1:
                                memo[string[:i+1]] = True
                                return True
                            else:
                                ans = checkString(string[i + 1:])
                                if ans:
                                    memo[string[i+1:]] = True
                                    return True
                    memo[string] = False
                    
                return False
            
        return checkString(s)
























#         setDict = set(wordDict)
#         memo = {}

#         def containsInDict(string):
#             return string in setDict

#         def checkString(string):
#             if len(string) == 1:
#                 memo[string] = containsInDict(string)
#                 return memo[string]
#             if string in memo:
#                 return memo[string]
#             else:
#                 for i in range(len(string)):
#                     if containsInDict(string[:i+1]):
#                         if i == len(string) - 1:
#                             memo[string] = True
#                             return True
#                         else: 
#                             ans = checkString(string[i+1:])
#                             if ans:
#                                 memo[string[i+1:]] = True
#                                 return True
                            
#                 memo[string] = False
#             return False

#         return checkString(s)
#         # O(len(s)^2) - time compl 
# # O(len(s)^2) - memory compl