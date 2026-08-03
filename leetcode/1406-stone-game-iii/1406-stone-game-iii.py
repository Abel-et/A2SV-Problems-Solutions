
from functools import lru_cache

class Solution:
    def stoneGameIII(self, stoneValue):
        n = len(stoneValue)

        @lru_cache(None)
        def dp(i):
            if i >= n:
                return 0

            best = float("-inf")
            total = 0

            for k in range(3):
                if i + k < n:
                    total += stoneValue[i + k]
                    best = max(best, total - dp(i + k + 1))

            return best

        ans = dp(0)

        if ans > 0:
            return "Alice"
        elif ans < 0:
            return "Bob"
        else:
            return "Tie"