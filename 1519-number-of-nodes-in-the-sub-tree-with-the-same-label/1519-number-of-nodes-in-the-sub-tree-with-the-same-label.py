class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        dic = defaultdict(list)
        for edge in edges:
            dic[edge[0]].append(edge[1])
            dic[edge[1]].append(edge[0])
            
        visited = [True]+[False]*(n-1)
        ans = [1]*n
        
        def dfs(node):
            temp = defaultdict(int)
            for i in dic[node]:
                if visited[i]: continue
                visited[i] = True
                dit = dfs(i)
                for i in dit.keys():
                    temp[i] += dit[i]
            temp[labels[node]] += 1
            ans[node] = temp[labels[node]]
            return temp
        
        dfs(0)
        return ans
                