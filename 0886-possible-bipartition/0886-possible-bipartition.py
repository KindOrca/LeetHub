class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        if len(dislikes) == 0: return True
        group = [[] for _ in range(n+1)]
        group_one = []
        group_two = []
        visited = [False] * (n+1)
        for dislike in dislikes:
            group[dislike[0]].append(dislike[1])
            group[dislike[1]].append(dislike[0])
        group_one.append(1)
        for i in range(1, n+1):
            ret = recursive(i, group_one, group_two, visited, group)
            if not ret: return False
        return True
    
def recursive(i, group_one, group_two, visited, group):
    if visited[i]: return True
    visited[i] = True
    for node in group[i]:
        if i in group_one:
            if node in group_one: return False
            if node not in group_two:
                group_two.append(node)
                recursive(node, group_one, group_two, visited, group)
        else:
            if node in group_two: return False
            if node not in group_one: 
                group_one.append(node)
                recursive(node, group_one, group_two, visited, group)
    return True
    