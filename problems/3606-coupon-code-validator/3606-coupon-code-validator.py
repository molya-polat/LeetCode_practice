class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        finalResultOfTuples = [] 
        allList = [chr(i) for i in range(ord('a'), ord('z') + 1)]
        allList += [chr(i) for i in range(ord('A'), ord('Z') + 1)]
        allList += [chr(i) for i in range(ord('0'), ord('9') + 1)]
        allList.append('_')
        allList = set(allList)
        businessLineValidList = {"electronics", "grocery", "pharmacy", "restaurant"}

        """
            set() - empty set
            {'a', 'c'} - set with elements
            {} - empty dictionary
            {'a': 1, 'b': 2} - dictionary with elements
        """

        for i in range(0, len(businessLine)):
            validCode = True
            if code[i] == "":
                validCode = False
            for c in code[i]:
                if c not in allList:
                    validCode = False
            validBusiness = businessLine[i] in businessLineValidList
            if validCode and validBusiness and isActive[i]:
                finalResultOfTuples.append((businessLine[i], code[i]))

        finalResult = []
        finalResultSortedTuples = sorted(finalResultOfTuples)
        for business, code in finalResultSortedTuples:
            finalResult.append(code)

        return finalResult