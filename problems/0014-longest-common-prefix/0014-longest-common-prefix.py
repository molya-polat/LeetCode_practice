class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common_prefix = strs[0]
        for word in strs:
            temp = ""
            for i in range(min(len(word), len(common_prefix))):
                if word[i] == common_prefix[i]:
                    temp += word[i]
                else:
                    break
            common_prefix = temp
            if common_prefix == "":
                return ""
        
        return common_prefix

        # O(n^2) - time
        # O(1) - space