class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        length1 = len(firstList)
        length2 = len(secondList)
      
        def intersection_between(start1, end1, start2, end2):
	        if start2 > end1 or start1 > end2:
	            return []
	        max_start = max(start1, start2)
	        min_end = min(end1, end2)
	        return [max_start, min_end]
    
        ans = []
        index1 = 0
        index2 = 0
        while index1 < length1 and index2 < length2:
            start1, end1 = firstList[index1]
            start2, end2 = secondList[index2]
            intersection = intersection_between(start1, end1, start2, end2)
            if len(intersection) > 0:
	            ans.append(intersection) 
            if end1 < end2:
	            index1 += 1
            elif end2 < end1:
	            index2 += 1
            else:
                index1 += 1
                index2 += 1
        return ans