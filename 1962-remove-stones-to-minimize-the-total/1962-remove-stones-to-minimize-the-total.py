class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        from queue import PriorityQueue
        l = len(piles)
        queue = PriorityQueue()
        for pile in piles:
            queue.put(-pile)
        for _ in range(k):
            val = ceil(-queue.get()/2)
            queue.put(-val)
        ans = 0
        for i in range(l):
            ans += -queue.get()
        return ans