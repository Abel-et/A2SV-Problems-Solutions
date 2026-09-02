class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        if len( nums1) == 1:
            return True


        even , odd = 0, 0

        for i in nums1:
            if i % 2 == 0 :
                even += 1
            else:
                odd += 1

    
        return True
        
