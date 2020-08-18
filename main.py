# This is a sample Python script.
from typing import List
import math


class Solution:
    def equalDistance(self, points: List[List[int]], k: int):
        if not points: return None

        dis_sum, dis_segment = self.distanceSum(points)
        print(dis_sum, dis_segment)
        L = dis_sum / k
        res = []
        remainder = 0

        # there are many cases to discuss between L and dis_segment
        for index, distance in enumerate(dis_segment):
            print('remainder :', remainder)
            cur_distance = distance + remainder
            print('cur_distance :', cur_distance)
            num_seg = int(cur_distance // L)
            if num_seg == 0:
                remainder += distance
                continue

            for i in range(0, num_seg):
                point = self.calculate_coordinate(points, (i + 1) * L - remainder, index, distance)
                print(point)
                res.append(point)

            remainder = cur_distance - num_seg * L
        return res

    def calculate_coordinate(self, points, L, index, seg):
        beta = L / seg

        x1, y1 = points[index][0], points[index][1]
        x2, y2 = points[index + 1][0], points[index + 1][1]

        x = beta * (x2 - x1) + x1
        y = beta * (y2 - y1) + y1

        return [x, y]

    def distanceSum(self, points):
        dis_sum = 0
        dis_segment = []

        for i in range(1, len(points)):  # 这里的range对不对？
            tmp = self.dis_twoPoints(points[i - 1], points[i])
            dis_segment.append(tmp)
            dis_sum += tmp

        return dis_sum, dis_segment

    def dis_twoPoints(self, p1, p2):
        x1, y1 = p1[0], p1[1]
        x2, y2 = p2[0], p2[1]

        return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    s = Solution()
    #print(s.equalDistance([[0,0], [5,0], [5,2], [10,2]], 3))
    print(s.equalDistance([[0, 0], [5, 0], [-5, 2], [10, 7]], 8))

