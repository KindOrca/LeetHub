class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        l = len(tasks)
        for i in range(l):
            tasks[i].append(i)
        tasks.sort(key=lambda x:(x[0],x[1],x[2]))
        time = tasks[0][0] + tasks[0][1]
        ans = [tasks[0][2]]
        heapq = []
        tasks = tasks[1:]
        while tasks:
            temp = tasks[0]
            if temp[0] <= time:
                heappush(heapq, (temp[1], temp[2]))
                tasks.pop(0)
            else:
                if not heapq:
                    time = tasks[0][0]
                    continue
                tup = heappop(heapq)
                ans.append(tup[1])
                time += tup[0]
        while heapq:
            ans.append(heappop(heapq)[1])
        return ans