class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        dic = defaultdict(int)
        for task in tasks:
            dic[task] += 1
        if 1 in dic.values(): return -1
        ans = 0
        for task in set(tasks):
            ans += dic[task]//3
            ans += 0 if dic[task]%3==0 else 1
        return ans