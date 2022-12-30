class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:        
        def dfs(now, queue):
            nonlocal ans
            nonlocal graph
            nonlocal visited
            for i in graph[now]:
                if i == len(graph)-1:
                    ans.append(queue+[i])
                    continue
                if visited[i]: continue
                visited[i] = True
                queue.append(i)
                dfs(i, queue)
                visited[i] = False
                queue.pop()
        ans = []          
        n = len(graph)
        visited = [True] + [False] * (n-1)
        queue = [0]
        dfs(0, queue)
        return ans