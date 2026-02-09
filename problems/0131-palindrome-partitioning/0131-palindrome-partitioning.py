class Solution:
    def partition(self, s: str) -> List[List[str]]:
        palindrome = {}
        def isPalindrome(string):
            if string in palindrome:
                return palindrome[string]
            if len(string) == 1:
                palindrome[string] = True
                return True
            for i in range(len(string) // 2):
                if string[i] != string[len(string) - i - 1]:
                    palindrome[string] = False
                    return False
            palindrome[string] = True
            return True

        def checkString(string):
            if len(string) == 1:
                return [[string]]
            result = []
            for i in range(len(string)):
                if isPalindrome(string[:i+1]):
                    if i == len(string) - 1:
                        newPartition = [string[:i+1]]
                        result.append(newPartition)
                        return result
                    partitionsRight = checkString(string[i+1:])
                    if len(partitionsRight) > 0:
                        for p in partitionsRight:
                            partition = [string[:i+1]]
                            partition.extend(p)
                            result.append(partition)
            return result
        
        return checkString(s)

        # O(n^2) - time
        # O(n^2) - space