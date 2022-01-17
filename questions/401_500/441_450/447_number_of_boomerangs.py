# coding=utf-8

from typing import List


class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        ans = 0
        for p in points:
            ans_dict = {}
            for q in points:
                distance = (p[0] - q[0]) * (p[0] - q[0]) + (p[1] - q[1]) * (p[1] - q[1])
                if distance in ans_dict:
                    ans_dict[distance] += 1
                else:
                    ans_dict.setdefault(distance, 1)
            for value in ans_dict.values():
                ans += value * (value - 1)
        return ans


if __name__ == '__main__':
    points = [[1,1]]
    c = Solution()
    ans = c.numberOfBoomerangs(points)
    print(ans)
