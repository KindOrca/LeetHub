class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        from collections import deque
        deq = deque()
        n = len(rooms)
        visited = [1] + [0]*(n-1)
        deq.append(0)
        while deq:
            now = deq.popleft()
            for i in rooms[now]:
                if visited[i]: continue
                visited[i] = 1
                deq.append(i)
        ans = True if sum(visited) == n else False
        return ans