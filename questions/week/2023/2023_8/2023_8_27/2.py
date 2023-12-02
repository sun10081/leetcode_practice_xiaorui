# -*- coding: utf-8 -*-
"""
@author: guoxiaorui
@file: 2
@time: 2023/8/27 10:29 AM
@desc:
"""
from typing import List
from collections import defaultdict


class Solution:
    def minimumPossibleSum(self, n: int, target: int) -> int:
        cnt = defaultdict(int)
        ans = []
        cur = 1
        while len(ans) < n:
            if cur < target and target - cur not in cnt:
                ans.append(cur)
                cnt[cur] = 1
            elif cur >= target:
                ans.append(cur)
                cnt[cur] = 1
            cur += 1
        print(ans)
        return sum(ans)


if __name__ == '__main__':
    n = 3
    target = 3
    s = Solution()
    print(s.minimumPossibleSum(n, target))

