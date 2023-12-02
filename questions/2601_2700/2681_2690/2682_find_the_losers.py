# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 2682_find_the_losers.py
@time: 2023-08-16 15:13:20 
"""
from typing import List
from collections import defaultdict


class Solution:
    def circularGameLosers(self, n: int, k: int) -> List[int]:
        cnt = defaultdict(int)
        time = 1
        cur = 1
        cnt[1] = 1

        while time:
            tmp = cur + k * time
            if tmp % n == 0:
                cur = n
            elif tmp > n:
                cur = tmp % n
            else:
                cur = tmp
            time += 1
            cnt[cur] += 1

            if cnt[cur] > 1:
                break

        ans = []
        for i in range(1, n + 1):
            if cnt[i] == 0:
                ans.append(i)
        return ans


class Solution2:
    def circularGameLosers(self, n: int, k: int) -> List[int]:
        ans = []
        i, j = k, 0
        visit = [False] * n

        while not visit[j]:
            visit[j] = True
            j = (i + j) % n
            i += k

        for i in range(n):
            if not visit[i]:
                ans.append(i + 1)
        return ans


if __name__ == '__main__':
    s = Solution2()
    n = 5
    k = 3
    print(s.circularGameLosers(n, k))