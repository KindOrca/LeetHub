class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        L = len(points)
        if L < 3: return L
        points = sorted(points, key=lambda x:(x[0],x[1]))
        print(points)
        ans = 2
        temp, x_val = 0, points[0][0]
        for x, _ in points:
            if x_val != x:
                ans = max(ans, temp)
                temp = 0
                x_val = x
            temp += 1
        ans = max(ans, temp)

        for i in range(L):
            x1, y1 = points[i]
            for j in range(i+1, L):
                x2, y2 = points[j]
                if x1 == x2: continue
                temp = 2
                slope = (y2 - y1) / (x2 - x1)
                y_intercept = y1 - slope*x1
                for k in range(j+1, L):
                    x3, y3 = points[k]
                    if x2 == x3: continue
                    if y3+0.00001 >= slope*x3 + y_intercept and y3-0.00001 <= slope*x3 + y_intercept:
                        temp += 1
                ans = max(ans, temp)
        return ans
                