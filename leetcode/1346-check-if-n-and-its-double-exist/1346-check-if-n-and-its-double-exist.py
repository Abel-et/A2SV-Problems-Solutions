class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        def binary_search(targe, index):
            left , right = 0 , len(arr) - 1

            while left <= right:
                mid = (left + right) //2

                if arr[mid] == target:
                    if mid == index:
                        return False
                    return True
                elif arr[mid] < target:
                    left = mid +1
                else:
                    right = mid -1
            return False
        arr.sort()
        for i in range(len(arr)):
            target = arr[i] * 2
            if binary_search(target,i):
                return True
            else:
                continue
        return False