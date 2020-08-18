class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:        return False

        row, col = len(matrix), len(matrix[0])

        i, j = row - 1, 0

        while 0 <= i < row and 0 <= j < col:
            if matrix[i][j] == target:
                return True
            if matrix[i][j] > target:
                i -= 1
            else:
                j += 1

        return False

    def searchMatrix2(self, matrix, target):
        if not matrix: return False

        row, col = len(matrix), len(matrix[0])
        x, y = 0, col - 1
        while 0 <= x < row and 0 <= y < col:
            if matrix[x][y] == target:
                return True
            if matrix[x][y] > target:
                y -= 1
            else:
                x += 1
        return False

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if not points: return 0
        res = 0
        while points:
            cur = points.pop()
            res = max(res, self.helper(cur, points))

        return res

    def helper(self, cur, points):
        x1, y1 = cur
        duplicate, count = 0, 0
        slope_map = {}

        for x2, y2 in points:
            if x1 == x2 and y1 == y2:
                duplicate += 1
            else:
                dx, dy = x2 - x1, y2 - y1
                slope = self.calculate_slope(dx, dy)
                slope_map[slope] = slope_map.get(slope, 0) + 1
                count = max(count, slope_map[slope])

        return count + duplicate + 1

    def calculate_slope(self, dx, dy):
        if dx == 0:
            return 'vertical'
        if dy == 0:
            return 'horizontal'
        g = math.gcd(dx, dy)
        return (dx / g, dy / g)