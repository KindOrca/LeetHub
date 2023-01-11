class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        if len(set(hasApple)) == 1 and not hasApple[0]:
            return 0
        visited = [True]+[False]*(n-1)
        dic = defaultdict(list)
        for edge in edges:
            dic[edge[0]].append(edge[1])
            dic[edge[1]].append(edge[0])

        def check(node, queue):
            for i in dic[node]:
                if visited[i]: continue
                visited[i] = True
                queue.append(i)
                if hasApple[i]:
                    ans.update(queue)
                check(i, queue)
                queue.pop(-1)

        ans = set()
        check(0, [])
        return 2*len(ans)