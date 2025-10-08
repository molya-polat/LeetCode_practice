class Solution:
    def generateSchedule(self, n: int) -> List[List[int]]:
        if n < 5:
            return []

        schedule = []
        matches = set()

        for i in range(n):
            for j in range(i + 1, n):
                matches.add((i, j))
                matches.add((j, i))

        def can_near(p1, p2):
            if p1[0] == p2[0] or p1[0] == p2[1] or p1[1] == p2[0] or p1[1] == p2[1]:
                return False
            return True

        def can_place_back(arr, p):
            if len(arr) == 0:
                return True
            if can_near(arr[len(arr) - 1], p):
                return True
            return False
        
        while len(matches) > 0:
            for pair in list(matches):
                if can_place_back(schedule, pair):
                    schedule.append(list(pair))
                    matches.remove(pair)
                else:
                    for day in range(len(schedule)):
                        if (day == 0 or can_near(schedule[day - 1], pair)) and can_near(schedule[day], pair):
                            schedule.insert(day, list(pair))
                            matches.remove(pair)
                            break
        
        return schedule

        # O(n^4) - time compl
        # O(n^2) - space compl