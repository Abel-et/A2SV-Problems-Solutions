import math
from typing import List

class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if n == 0 or k == 0:
            return 0
            
        # 1. Build a Sparse Table for O(1) Range Max and Min Queries
        K = int(math.log2(n)) + 1
        st_max = [[0] * K for _ in range(n)]
        st_min = [[0] * K for _ in range(n)]
        
        for i in range(n):
            st_max[i][0] = nums[i]
            st_min[i][0] = nums[i]
            
        for j in range(1, K):
            for i in range(n - (1 << j) + 1):
                st_max[i][j] = max(st_max[i][j-1], st_max[i + (1 << (j-1))][j-1])
                st_min[i][j] = min(st_min[i][j-1], st_min[i + (1 << (j-1))][j-1])
                
        def query_val(l: int, r: int) -> int:
            if l > r: return 0
            length = r - l + 1
            j = int(math.log2(length))
            mx = max(st_max[l][j], st_max[r - (1 << j) + 1][j])
            mn = min(st_min[l][j], st_min[r - (1 << j) + 1][j])
            return mx - mn

        # 2. Count helper: Returns number of subarrays with value >= X
        # For a fixed right endpoint 'r', the subarray value max - min is monotonic 
        # as the left endpoint 'l' decreases. We can use a two-pointer approach.
        def count_subarrays_with_value_at_least(X: int) -> int:
            count = 0
            l = 0
            for r in range(n):
                # Move 'l' forward while the value of subarray nums[l..r] is >= X
                while l <= r and query_val(l, r) >= X:
                    l += 1
                # All subarrays from index 0 to l-1 ending at r have a value >= X
                count += l
            return count

        # 3. Binary Search for the threshold score X
        low, high = 0, max(nums) - min(nums)
        threshold = 0
        
        while low <= high:
            mid = (low + high) // 2
            if count_subarrays_with_value_at_least(mid) >= k:
                threshold = mid
                low = mid + 1
            else:
                high = mid - 1
                
        # 4. Sum helper: Sums up all subarray values strictly greater than target X
        # We also collect how many such items exist to fill the remainder quota using X.
        total_sum = 0
        items_counted = 0
        l = 0
        
        for r in range(n):
            while l <= r and query_val(l, r) > threshold:
                l += 1
            # Subarrays starting from 0 up to l-1 ending at r have value > threshold
            items_counted += l
            # Accumulate their actual explicit values
            for i in range(l):
                total_sum += query_val(i, r)
                
        # Fill remaining slots up to k elements using the threshold value
        remaining_slots = k - items_counted
        total_sum += remaining_slots * threshold
        
        return total_sum
