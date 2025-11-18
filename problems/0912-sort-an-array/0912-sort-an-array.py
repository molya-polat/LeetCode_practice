class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def merge(arr1, arr2):

            arr = [0 for _ in range(len(arr1) + len(arr2))]
            j = 0
            k = 0
            for i in range(len(arr)):
                if j >= len(arr1) and k < len(arr2):
                    arr[i] = arr2[k]
                    k += 1
                elif k >= len(arr2) and j < len(arr1):
                    arr[i] = arr1[j]
                    j += 1
                elif j < len(arr1) and k < len(arr2):
                    if arr1[j] < arr2[k]:
                        arr[i] = arr1[j]
                        j += 1
                    else:
                        arr[i] = arr2[k]
                        k += 1
            return arr

        def divide(arr):
            medium = len(arr) // 2
            left_arr = arr[:medium]
            right_arr = arr[medium:]
            if len(left_arr) > 1: 
                left_arr = divide(left_arr)
            if len(right_arr) > 1:
                right_arr = divide(right_arr)
            
            return merge(left_arr, right_arr)
        
        return divide(nums)