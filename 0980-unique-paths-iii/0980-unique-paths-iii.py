class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        self.ans = 0
        l, w = len(grid), len(grid[0])
        moveUD = [-1,1,0,0]
        moveLR = [0,0,-1,1]
        visited = [[False for _ in range(w)] for _ in range(l)]
        obstacle = []
        for i in range(l):
            for j in range(w):
                if grid[i][j] == 0: continue
                if grid[i][j] == 1:
                    (s1, s2) = (i,j)
                elif grid[i][j] == 2:
                    (e1, e2) = (i,j)
                else:
                    obstacle.append((i,j))

        visited[s1][s2] = True

        def dfs(p1, p2, cnt):
            nonlocal visited
            if p1 == e1 and p2 == e2:
                if cnt == l*w - len(obstacle):
                    self.ans += 1
                return
            for i, j in zip(moveUD, moveLR):
                hie, wid = p1+i, p2+j
                if hie < 0 or wid < 0 or hie >= l or wid >= w or visited[hie][wid]: continue
                if (hie, wid) in obstacle: continue
                visited[hie][wid] = True
                ans = dfs(hie, wid, cnt+1)
                visited[hie][wid] = False
        dfs(s1, s2, 1)

        return self.ans