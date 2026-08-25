class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        largest = max(nums)

        for i in range(1,largest):
            if k*i not in nums:
                return k*i
        return largest * k if k != 1 else largest + 1
