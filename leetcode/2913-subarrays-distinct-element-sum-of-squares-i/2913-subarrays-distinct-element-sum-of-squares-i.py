class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        total = 0
        for i in range(len(nums)):
            for j in range(i,  len(nums)):
                distinct = set(nums[i:j+1])
                total += len(distinct) * len(distinct)
        return total