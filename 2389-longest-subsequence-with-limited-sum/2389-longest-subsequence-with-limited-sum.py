class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        ans = [0] * len(queries)
        nums = sorted(nums)
        n = len(nums)
        cache = [0] * n
        cache[0] = nums[0]
        for i in range(1, n):
            cache[i] = cache[i-1] + nums[i]
        for idx, query in enumerate(queries):
            for i, var in enumerate(cache, start=1):
                if query >= var:
                    ans[idx] = i
                else: break
        return ans
        