class Solution:
    def maxJumps(self, arr: list[int], d: int) -> int:
        n = len(arr)
        memo = [-1] * n
        
        def dfs(i: int) -> int:
            if memo[i] != -1:
                return memo[i]
            
            max_steps = 1
            
            # Explore jumps to the right
            for j in range(i + 1, min(i + d + 1, n)):
                if arr[j] >= arr[i]:
                    break  # Blocked by a taller or equal bar
                max_steps = max(max_steps, 1 + dfs(j))
                
            # Explore jumps to the left
            for j in range(i - 1, max(i - d - 1, -1), -1):
                if arr[j] >= arr[i]:
                    break  # Blocked by a taller or equal bar
                max_steps = max(max_steps, 1 + dfs(j))
                
            memo[i] = max_steps
            return max_steps

        # Find the maximum value starting from any index
        return max(dfs(i) for i in range(n))
