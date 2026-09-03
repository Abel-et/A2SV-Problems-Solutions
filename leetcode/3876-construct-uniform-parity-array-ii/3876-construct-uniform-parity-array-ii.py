class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        check = min(nums1)

        if check % 2 == 0 :

            for i in nums1:
                if i == check or  i % 2 == 0: 
                    continue
                if i - check <= 1 or (i - check) % 2 == 1:
                    return False
            else:
                return True
        else:
            for i in nums1:
                if i == check  or i % 2 == 1:
                    continue
                if i - check < 1 or (i - check) % 2 == 0:
                    print(i, check, i-check)
                    return False
            return True