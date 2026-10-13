class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        # remove all negative values for nums 
        for i in range(len(nums)):
            if nums[i] <  0 :
                nums[i] = -1 * nums[i]
        
        # sort nums assending order 
        nums.sort()

        # put to pointer for left and right subtract larges to smallest number 
        total , left, right = 0 , 0 , len(nums) - 1

        while left < right:
            print(nums[right], nums[left])
            total += nums[right] ** 2 - nums[left] ** 2
            left +=1
            right -=1
        
        # if len of nums is odd the middle element should be added 
        if len(nums) % 2 == 1:
            total += nums[left] ** 2
        return total