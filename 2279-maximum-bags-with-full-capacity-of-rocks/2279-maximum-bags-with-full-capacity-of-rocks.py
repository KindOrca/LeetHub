class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        surplus = sorted([c-r for c,r in zip(capacity, rocks)])
        ans = 0
        for i, sur in enumerate(surplus, start=1):
            additionalRocks -= sur
            if additionalRocks < 0:
                ans = i-1
                break
        else: return len(capacity)
        return ans