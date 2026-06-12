class Solution:
    def assignEdgeWeights(self, edges: list[list[int]], queries: list[list[int]]) -> list[int]:
        # Derive n from the tree property: edges = n - 1
        n = len(edges) + 1
        MOD = 10**9 + 7
        
        # Step 1: Build the Adjacency List
        adj = [[] for _ in range(n + 1)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            
        # Step 2: Precompute Binary Lifting Table & Depths
        LOG = 18  
        up = [[0] * LOG for _ in range(n + 1)]
        depth = [0] * (n + 1)
        
        # BFS to initialize depth and immediate parents
        queue = [1]
        visited = {1}
        depth[1] = 0
        up[1][0] = 1 
        
        head = 0
        while head < len(queue):
            curr = queue[head]
            head += 1
            for neighbor in adj[curr]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    depth[neighbor] = depth[curr] + 1
                    up[neighbor][0] = curr
                    queue.append(neighbor)
                    
        # Fill the binary lifting sparse table
        for j in range(1, LOG):
            for i in range(1, n + 1):
                up[i][j] = up[up[i][j-1]][j-1]
                
        # LCA Helper Function
        def get_lca(u, v):
            if depth[u] < depth[v]:
                u, v = v, u
            diff = depth[u] - depth[v]
            for j in range(LOG):
                if (diff >> j) & 1:
                    u = up[u][j]
            if u == v:
                return u
            for j in range(LOG - 1, -1, -1):
                if up[u][j] != up[v][j]:
                    u = up[u][j]
                    v = up[v][j]
            return up[u][0]
            
        # Step 3: Precompute Powers of 2
        pow2 = [1] * (n + 1)
        for i in range(1, n + 1):
            pow2[i] = (pow2[i-1] * 2) % MOD
            
        # Step 4: Process Queries
        answer = []
        for u, v in queries:
            if u == v:
                answer.append(0)
            else:
                lca = get_lca(u, v)
                k = depth[u] + depth[v] - 2 * depth[lca]
                answer.append(pow2[k - 1])
                
        return answer