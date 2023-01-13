class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        L = len(parent)
        ans = 1
        dic = defaultdict(list)
        for i in range(1, L):
            dic[parent[i]].append(i)

        def check(node):
            nonlocal ans
            ret = []
            for i in dic[node]:
                temp = check(i)
                if s[node] != s[i]:
                    ret.append(temp)
            ret.sort()
            if len(ret) == 1: 
                ans = max(ans, ret[0] + 1)
                return ret[0] + 1
            elif len(ret) > 1:
                ans = max(ans, ret[-1]+ret[-2]+1)
                return ret[-1] + 1
            return 1

        check(0)
        return ans