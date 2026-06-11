from collections import deque
class Solution:
    def assignEdgeWeights(self, edges: List[List[int]]) -> int:
        if not edges:
            return 0

        # building adjacency list
        graph = {}
        for u , v in edges:
            graph.setdefault(u,[]).append(v)
            graph.setdefault(v, []).append(u)
        
        # finding max depth uisng bfs
        queue = deque([(1,0)]) # (current_node , current_depth)
        visited = {1}
        max_depth = 0

        while queue:
            node ,depth = queue.popleft()
            max_depth = max(max_depth , depth)

            for nig in graph.get(node,[]):
                if nig not in visited:
                    visited.add(nig)
                    queue.append((nig, depth + 1))
        MOD = 10**9 + 7

        return pow(2,max_depth-1, MOD)
        