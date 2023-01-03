class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        cnt = 0
        for i in range(len(strs[0])):
            temp = 0
            for let in strs:
                if ord(let[i]) < temp:
                    cnt += 1
                    break
                temp = ord(let[i])
        return cnt