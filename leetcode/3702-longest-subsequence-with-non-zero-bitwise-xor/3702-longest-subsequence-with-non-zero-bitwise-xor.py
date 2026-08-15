class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        # Check if the array contains only zeros
        if all(x == 0 for x in nums):
            return 0
        
        # Calculate the XOR sum of all elements
        total_xor = 0
        for num in nums:
            total_xor ^= num
            
        # If total XOR is non-zero, keep the whole array
        if total_xor != 0:
            return len(nums)
        
        # If total XOR is zero, remove exactly one non-zero element
        return len(nums) - 1
