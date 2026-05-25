class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)
        if s[n - 1] == '1':
            return False
            
        # dp[i] will be True if index i is reachable
        dp = [False] * n
        dp[0] = True
        
        # reachable_count tracks the number of reachable indices 
        # inside the current jumping window
        reachable_count = 0
        
        for i in range(1, n):
            # Add the new index entering the window from the right side
            if i >= minJump and dp[i - minJump]:
                reachable_count += 1
                
            # Remove the old index leaving the window from the left side
            if i > maxJump and dp[i - maxJump - 1]:
                reachable_count -= 1
                
            # If s[i] is '0' and there is at least one reachable index 
            # in the jumping window, then index i is reachable
            if s[i] == '0' and reachable_count > 0:
                dp[i] = True
                
        return dp[n - 1]
