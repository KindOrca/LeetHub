class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            
        closer_nodes_count = [0] * n
        ans = [0] * n
        visited = set()
        def dfs(cur):
            nonlocal closer_nodes_count, ans
            closer_nodes = 1 
            
            for child in graph[cur]:
                if child not in visited:
                    visited.add(child)
                    child_nodes_count = dfs(child)
                    closer_nodes += child_nodes_count
                    ans[0] += child_nodes_count
            
            closer_nodes_count[cur] = closer_nodes
            
            return closer_nodes
        
        visited.add(0)
        dfs(0)
        
        def dfs2(cur):
            nonlocal ans
            for child in graph[cur]:
                if child not in visited:
                    visited.add(child)
                    ans[child] = ans[cur] - closer_nodes_count[child] + (n - closer_nodes_count[child])
                    dfs2(child)
        
        visited = set()
        visited.add(0)
        dfs2(0)
        
        return ans