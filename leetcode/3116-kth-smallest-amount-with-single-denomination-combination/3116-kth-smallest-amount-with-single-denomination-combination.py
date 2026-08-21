
from math import gcd
from itertools import combinations
from typing import List

class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        # Helper function to calculate LCM
        def lcm(a: int, b: int) -> int:
            return (a * b) // gcd(a, b)
        
        # Precompute LCMs for all possible combinations of coins
        # Grouped by the number of coins in the combination
        n = len(coins)
        lcm_cache = []
        for r in range(1, n + 1):
            level = []
            for combo in combinations(coins, r):
                curr_lcm = combo[0]
                for coin in combo[1:]:
                    curr_lcm = lcm(curr_lcm, coin)
                level.append(curr_lcm)
            lcm_cache.append(level)
            
        # Helper function to count unique multiples <= target
        def count_multiples(target: int) -> int:
            total_count = 0
            for r in range(1, n + 1):
                # Add for odd sizes, subtract for even sizes
                sign = 1 if r % 2 != 0 else -1
                for current_lcm in lcm_cache[r - 1]:
                    total_count += sign * (target // current_lcm)
            return total_count

        # Binary search range
        low = min(coins)
        high = min(coins) * k
        ans = high
        
        while low <= high:
            mid = (low + high) // 2
            if count_multiples(mid) >= k:
                ans = mid
                high = mid - 1  # Try to find a smaller valid amount
            else:
                low = mid + 1   # Increase the lower bound
                
        return ans
