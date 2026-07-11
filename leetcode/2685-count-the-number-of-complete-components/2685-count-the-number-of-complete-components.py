class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        
        # build an adj graph 
        graph = [[] for _ in  range(n)]
        for v , u in edges:
            graph[v].append(u)
            graph[u].append(v)

        # create an array that telles the conection and component var
        visited = [False for _ in range(n)]
        completed = 0

        # creating dfs travesing every connected nodes 
        def dfs (node , graph , visited):
            visited[node] = True
            component.append(node)
            for nieg in graph[node]:
                if not visited[nieg]:
                    dfs(nieg, graph , visited)

        # travers to each node 

        for i in range(n):
            if not visited[i]:
                component = []
                dfs(i ,graph ,visited)

                # formula of completed graph nodes*(nodes-1) //2:
                nodes = len(component)
                edge_count = 0

                for node in component:
                    edge_count += len(graph[node])
                edge_count //= 2

                if edge_count == nodes*(nodes - 1) // 2:
                    completed += 1

        return completed