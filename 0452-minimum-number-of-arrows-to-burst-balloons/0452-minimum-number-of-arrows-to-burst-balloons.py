class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        cnt = 0
        points = sorted(points, key=lambda x:x[1])
        pivot = -2147483649
        for point in points:
            if pivot < point[0]:
                pivot = point[1]
                cnt += 1
        return cnt
                
            