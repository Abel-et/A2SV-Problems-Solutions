class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        k = sum(nums) - x
        if k < 0 : return -1
        best = -1
        s = i = 0 

        for j , num in enumerate(nums):
            s += num
            while s > k :
                s -= nums[i]
                i += 1
            if s == k :
                best = max(best, j - i + 1)
        return -1 if best < 0 else len(nums) - best 
        