from collections import deque
import heapq
class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        n = len(grid)
    
        # If the start or end cell contains a thief, safeness factor is 0
        if grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return 0
            
        # Step 1: Multi-source BFS to calculate minimum distance to any thief
        dist = [[float('inf')] * n for _ in range(n)]
        queue = deque()
        
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    dist[r][c] = 0
                    queue.append((r, c))
                    
        directions = [((0, 1)), ((0, -1)), ((1, 0)), ((-1, 0))]
        
        while queue:
            r, c = queue.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and dist[nr][nc] == float('inf'):
                    dist[nr][nc] = dist[r][c] + 1
                    queue.append((nr, nc))
                    
        # Step 2: Max-Priority Queue (Dijkstra) to find the maximum safeness path
        # Python heapq is a min-heap, so we store negative values to simulate a max-heap
        max_heap = [(-dist[0][0], 0, 0)]
        visited = [[False] * n for _ in range(n)]
        visited[0][0] = True
        
        while max_heap:
            d, r, c = heapq.heappop(max_heap)
            current_safeness = -d
            
            # Reached the destination
            if r == n - 1 and c == n - 1:
                return current_safeness
                
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc]:
                    visited[nr][nc] = True
                    # The safeness of a path is limited by its minimum distance cell
                    next_safeness = min(current_safeness, dist[nr][nc])
                    heapq.heappush(max_heap, (-next_safeness, nr, nc))
                    
        return 0