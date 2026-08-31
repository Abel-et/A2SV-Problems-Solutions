class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2:
            return n
            
        # Get indices of min and max elements
        idx1 = nums.index(min(nums))
        idx2 = nums.index(max(nums))
        
        # Ensure idx1 is always the smaller index (leftmost)
        i = min(idx1, idx2)
        j = max(idx1, idx2)
        
        # Option 1: Remove both from the front
        from_front = j + 1
        
        # Option 2: Remove both from the back
        from_back = n - i
        
        # Option 3: Remove i from front, j from back
        from_both = (i + 1) + (n - j)
        
        # Return the absolute minimum of the three strategies
        return min(from_front, from_back, from_both)
