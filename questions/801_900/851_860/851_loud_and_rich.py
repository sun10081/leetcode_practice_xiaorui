# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 851_loud_and_rich
@time: 2021/12/15 10:43 上午
@desc: 
"""
from typing import List


class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        def dfs(x: int):
            if ans[x] != -1:
                return
            ans[x] = x
            for y in more_rich[x]:
                dfs(y)
                if quiet[ans[y]] < quiet[ans[x]]:
                    ans[x] = ans[y]

        n = len(quiet)
        ans = [-1] * n
        more_rich = [[] for _ in range(n)]
        for person_a, person_b in richer:
            more_rich[person_b].append(person_a)

        for i in range(n):
            dfs(i)
        return ans


class Solution2:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        pass


if __name__ == '__main__':
    richer = [[1, 0], [2, 1], [3, 1], [3, 7], [4, 3], [5, 3], [6, 3]]
    quiet = [3, 2, 5, 4, 6, 1, 7, 0]
    s = Solution()
    print(s.loudAndRich(richer, quiet))
