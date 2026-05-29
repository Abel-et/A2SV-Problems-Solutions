class Solution:
    def minElement(self, nums):
        # Function to calculate digit sum
        def digit_sum(n):
            return sum(int(d) for d in str(n))
        
        # Replace each number with digit sum
        nums = [digit_sum(x) for x in nums]
        
        # Return minimum element
        return min(nums)