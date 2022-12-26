class Solution:
    def canJump(self, nums: List[int]) -> bool:
        l = len(nums)
        idx, max_idx = 0, nums[0]
        while max_idx < l:
            temp = max_idx
            for i in range(idx, max_idx+1):
                max_idx = max(max_idx, i+nums[i])
                if max_idx >= l-1: break
            idx = temp
            if idx == max_idx: break
        if max_idx >= l-1: return True
        return False