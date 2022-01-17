# coding=utf-8

from typing import List
from collections import defaultdict


class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        """
        大矩形面积等于各小矩形面积和
        大矩形四顶点只出现一次，其余顶点出现2或者4次
        :param rectangles:
        :return:
        """
        area = 0
        min_x = rectangles[0][0]
        min_y = rectangles[0][1]
        max_x = rectangles[0][2]
        max_y = rectangles[0][3]
        cnt = defaultdict(int)

        for rect in rectangles:
            x = rect[0]
            y = rect[1]
            a = rect[2]
            b = rect[3]
            area = area + (a - x) * (b - y)
            min_x = min(min_x, x)
            min_y = min(min_y, y)
            max_x = max(max_x, a)
            max_y = max(max_y, b)

            cnt[(x, y)] += 1
            cnt[(x, b)] += 1
            cnt[(a, y)] += 1
            cnt[(a, b)] += 1

        if area != (max_x - min_x) * (max_y - min_y) or cnt[(min_x, min_y)] != 1 or cnt[(min_x, max_y)] != 1 or cnt[(max_x, min_y)] != 1 or cnt[(max_x, max_y)] != 1:
            return False
        # 删除4个顶点坐标
        del cnt[(min_x, min_y)], cnt[(min_x, max_y)], cnt[(max_x, min_y)], cnt[(max_x, max_y)]
        cnt_res = all(c == 2 or c == 4 for c in cnt.values())
        return cnt_res


if __name__ == '__main__':
    rectangles = [[1, 1, 3, 3], [3, 1, 4, 2], [3, 2, 4, 4], [1, 3, 2, 4], [2, 3, 3, 4]]
    s = Solution()
    print(s.isRectangleCover(rectangles))