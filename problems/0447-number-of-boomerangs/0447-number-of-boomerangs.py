class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        counter = 0
        diction = {}
        for i in range(len(points) - 1):
            for j in range(i + 1, len(points)):
                s = (points[j][0] - points[i][0])**2 + (points[j][1] - points[i][1])**2
                if s in diction:
                    c = 0
                    for pair in diction[s]:
                        if pair[0] == i or pair[1] == i or pair[0] == j or pair[1] == j:
                            c += 1
                    if c!= 0 :
                        counter += 2 * c 
                    diction[s].append((i, j))
                else:
                    diction[s] = [(i, j)]
            
        
        return counter

        # O(n^2) - time
        # O(n^2) - memory