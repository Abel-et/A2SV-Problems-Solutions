class Solution:
    def stoneGameVIII(self, stones: List[int]) -> int:
        n = len(stones)
        
        # Step 1: Calculate prefix sums in-place to save space
        for i in range(1, n):
            stones[i] += stones[i - 1]
            
        # Step 2: Initialize base case
        # If forced to take all stones, the score is the total sum
        max_diff = stones[-1]
        
        # Step 3: Iterate backwards from the second-to-last stone down to index 1
        for i in range(n - 2, 0, -1):
            max_diff = max(max_diff, stones[i] - max_diff)
            
        return max_diff
