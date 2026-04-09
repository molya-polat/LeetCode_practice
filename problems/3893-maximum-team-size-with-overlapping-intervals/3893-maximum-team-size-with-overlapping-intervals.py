class Solution:
    def maximumTeamSize(self, startTime: list[int], endTime: list[int]) -> int:
        sorted_start = sorted(startTime)
        sorted_end = sorted(endTime)
        ans_mx = 0
        n = len(startTime)

        def at_point_start_less_eq(end):
            return bisect.bisect_right(sorted_start, end)

        def at_point_end_less(start):
            return bisect.bisect_left(sorted_end, start)

        for i in range(n):
            start = startTime[i]
            end = endTime[i]

            cur_employees = at_point_start_less_eq(end) - at_point_end_less(start)
            ans_mx = max(ans_mx, cur_employees)

        return ans_mx