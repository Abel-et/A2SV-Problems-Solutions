from typing import List
from collections import Counter

class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        n = len(nums)
        subarray_counts = Counter()
        
        # Loop through every valid starting index of a window of size k
        for i in range(n - k + 1):
            # Extract the current window
            window = nums[i : i + k]
            # Use set() to count each unique number only ONCE per subarray
            for num in set(window):
                subarray_counts[num] += 1
                
        # Find the maximum number that appeared in exactly 1 subarray
        ans = -1
        for num, count in subarray_counts.items():
            if count == 1:
                ans = max(ans, num)
                
        return ans
