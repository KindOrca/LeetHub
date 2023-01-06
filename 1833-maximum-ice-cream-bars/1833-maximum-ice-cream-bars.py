class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs = sorted(costs)
        cnt = 0
        for cost in costs:
            if cost > coins: break
            coins -= cost
            cnt += 1
        return cnt