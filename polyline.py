from typing import List
import math


class Polyline:

    def equalDistance(self, points: List[List[int]], k: int):
        """
        # 1. Calculate all the segmentation distance and the total distance
        # 2. get the equal distance
        # 3. Discuss each condition and Calulate their coordinate
        """
        if not points: return None

        segments, totalDis = self.calculate_distance(points)

        # calculate the average
        L = totalDis / k

        remainder = 0
        res = []
        for index, each_seg in enumerate(segments):

            cur_distance = each_seg + remainder
            print(cur_distance)
            partition_num = int(cur_distance // L)

            if partition_num == 0:
                remainder += each_seg
                continue

            for i in range(partition_num):
                point = self.caculate_coordinate(points, index, (i + 1) * L - remainder, each_seg)
                res.append(point)

            remainder = cur_distance - partition_num * L
        return res

    def caculate_coordinate(self, points, index, L, seg):
        beta = L / seg

        x1, y1 = points[index][0], points[index][1]
        x2, y2 = points[index + 1][0], points[index + 1][1]

        x = beta * (x2 - x1) + x1
        y = beta * (y2 - y1) + y1

        return [x, y]

    def calculate_distance(self, points):
        seg_distance = []
        total_distance = 0

        for i in range(1, len(points)):
            tmp = self.euclidean(points[i], points[i - 1])
            seg_distance.append(tmp)
            total_distance += tmp

        return seg_distance, total_distance

    def euclidean(self, p1, p2):
        x1, y1 = p1[0], p1[1]
        x2, y2 = p2[0], p2[1]

        return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

if __name__ == '__main__':
    s = Polyline()
    #print(s.equalDistance([[0,0], [5,0], [5,2], [10,2]], 3))
    print(s.equalDistance([[0, 0], [5, 0], [-5, 2], [10, 7]], 8))