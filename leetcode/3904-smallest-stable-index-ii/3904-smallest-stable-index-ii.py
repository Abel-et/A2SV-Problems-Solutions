class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        
        # Precompute suffix minimums
        suff_min = [0] * n
        suff_min[-1] = nums[-1]
        for i in range(n - 2, -1, -1):
            suff_min[i] = min(nums[i], suff_min[i + 1])
            
        # Track running prefix max from left to right
        pref_max = nums[0]
        for i in range(n):
            pref_max = max(pref_max, nums[i])
            if pref_max - suff_min[i] <= k:
                return i
                
        return -1