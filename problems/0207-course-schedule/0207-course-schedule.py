class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not prerequisites:
            return True
        diction = defaultdict(set)
        for course, precourse in prerequisites:
            diction[course].add(precourse)
        
        studied = set()
        considered = set()
        not_studied = set()
        def study(course):
            considered.add(course)
            if course not in diction:
                studied.add(course)
            else:
                for prereq in diction[course]:
                    if prereq not in studied and prereq not in considered:
                        study(prereq)
                    elif prereq not in studied and prereq in considered:
                        not_studied.add(prereq)
                        return
                studied.add(course)
                        
        for i in range(numCourses):
            study(i)

        if len(studied) == numCourses and not not_studied:
            return True
        return False

        # O(n) - time
        # O(n) - space