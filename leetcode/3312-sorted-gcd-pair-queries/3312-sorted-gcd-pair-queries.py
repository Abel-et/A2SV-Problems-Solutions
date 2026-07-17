
import bisect
from typing import List

class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        max_val = max(nums)
        
        # Step 1: Count frequencies of each number
        cnt = [0] * (max_val + 1)
        for x in nums:
            cnt[x] += 1
            
        # Step 2: Count how many numbers are multiples of each g
        c = [0] * (max_val + 1)
        for g in range(1, max_val + 1):
            for m in range(g, max_val + 1, g):
                c[g] += cnt[m]
                
        # Step 3: Compute exact number of pairs with GCD = g
        exact_gcd = [0] * (max_val + 1)
        for g in range(max_val, 0, -1):
            total_pairs = c[g] * (c[g] - 1) // 2
            # Subtract pairs that have a strictly greater multiple of g as their GCD
            for m in range(2 * g, max_val + 1, g):
                total_pairs -= exact_gcd[m]
            exact_gcd[g] = total_pairs
            
        # Step 4: Build prefix sums of the frequencies of GCDs
        pref = [0] * (max_val + 1)
        for g in range(1, max_val + 1):
            pref[g] = pref[g - 1] + exact_gcd[g]
            
        # Step 5: Answer each query using binary search
        ans = []
        for q in queries:
            # We look for the first g where pref[g] > q
            g = bisect.bisect_right(pref, q)
            ans.append(g)
            
        return ans
