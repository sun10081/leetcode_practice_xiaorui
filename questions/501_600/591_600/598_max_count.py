# coding=utf-8


from typing import List


class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        min_m = m
        min_n = n
        for op in ops:
            min_m = min(min_m, op[0])
            min_n = min(min_n, op[1])
        return min_n * min_m


if __name__ == '__main__':
    m = 3
    n = 3
    ops = [[2, 2], [3, 3]]
    s = Solution()
    print(s.maxCount(m, n, ops))
