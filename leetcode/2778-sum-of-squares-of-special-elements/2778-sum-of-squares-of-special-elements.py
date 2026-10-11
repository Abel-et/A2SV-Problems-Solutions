class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        return sum( [ nums[s] * nums[s] for s in range(len(nums)) if len(nums) % (s+1) == 0])
        # n = len(nums)
        # ans = 0
        # for i in range(n):
        #     if n % (i+1) == 0:
        #         ans += (nums[i] * nums[i])
        # return ans