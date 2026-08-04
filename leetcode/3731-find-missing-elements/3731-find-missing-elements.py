class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        max_num = max(nums)
        min_num = min(nums)
        ans  = []
        for i in range(min_num, max_num):
            if i not in nums:
                ans.append(i)
        return ans