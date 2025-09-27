class Solution:
    totalNumbers = lambda self, d: \
        len({a * 100 + b * 10 + c \
            for i, a in enumerate(d) \
                for j, b in enumerate(d) \
                    for k, c in enumerate(d) \
                        if a != 0 and c % 2 == 0 and len({i, j, k}) == 3})



        # counter = 0
        # dictionary = Counter(digits)
        
        # for i in range(100, 1000, 2):
        #     tempDict = dict(dictionary)
        #     valid = True
        #     while i > 0:
        #         digit = i % 10
        #         if digit not in tempDict or tempDict[digit] <= 0:
        #             valid = False
        #             break
        #         else:
        #             tempDict[digit] -= 1
        #         i = i // 10
        #     if valid:
        #         counter += 1
            
        # return counter