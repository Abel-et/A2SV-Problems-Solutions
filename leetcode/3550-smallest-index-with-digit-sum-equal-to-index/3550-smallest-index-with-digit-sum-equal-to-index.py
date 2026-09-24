class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            s = str(nums[i])
            if len(s) > 1:
                k = 0 
                for j in s:
                    k += int(j)
                if k == i :
                    return i 
            else:
                if nums[i] == i:
                    return i 
        return  -1 