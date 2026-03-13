class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        sorted_arr = sorted(arr, key = lambda a: abs(a - x))
        sorted_arr = sorted_arr[:k]
        
        return sorted(sorted_arr)
        # ans = []
        # start = 0
        # end = len(arr) - 1
        # med = (start + end) // 2
        # if x < arr[0]:
        #     return arr[:k]
        # if x > arr[-1]:
        #     return arr[len(arr) - k:]
        # while start < end and med >= 0 and med < len(arr):
        #     if arr[med] > x:
        #         end  = med - 1
        #     elif arr[med] < x:
        #         start = med + 1
        #     else:
        #         start = med
        #         break
        #     med = (start + end) // 2
        
        # if arr[start] != x and abs(arr[start - 1] - x) <= abs(arr[start] - x):
        #     start = start - 1
        # if arr[start] != x and abs(arr[start + 1] - x) < abs(arr[start] - x):
        #     start = start + 1
        # stack = [arr[start]]
        # incr_left, incr_right = 1, 1
        # while start - incr_left >= 0 or start + incr_right < len(arr):
        #     if start - incr_left >= 0 and start + incr_right < len(arr):
        #         if abs(arr[start - incr_left] - x) < abs(arr[start + incr_right] - x):
        #             stack.append(arr[start - incr_left])
        #             incr_left += 1
        #         elif abs(arr[start - incr_left] - x) > abs(arr[start + incr_right] - x):
        #             stack.append(arr[start + incr_right])
        #             incr_right += 1
        #         else:
        #             stack.append(arr[start - incr_left])
        #             incr_left += 1
        #     elif start - incr_left >= 0:
        #         stack.append(arr[start - incr_left])
        #         incr_left += 1
        #     else:
        #         stack.append(arr[start + incr_right])
        #         incr_right += 1

        # sorted_result = sorted(stack[:k])
        # return sorted_result