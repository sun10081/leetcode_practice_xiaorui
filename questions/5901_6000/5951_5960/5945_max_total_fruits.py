# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 5945_max_total_fruits
@time: 2021/12/12 8:38 下午
@desc: 
"""
from typing import List
from collections import deque


class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        n = len(fruits)
        ans = 0
        queue = deque([])
        point = 0
        # 先从左边开始，找到能够到达的最远点，并把从最远的开始到startPos的所有水果加起来，同时入队
        while point < n and fruits[point][0] <= startPos:
            if startPos - fruits[point][0] <= k:
                ans += fruits[point][1]
                queue.append((fruits[point][0], fruits[point][1]))
            point += 1
        tmp = ans
        while point < n and fruits[point][0] - startPos <= k:
            # 对于每一个startPos右端的水果，依次检查左端点是否满足条件
            # 画图可知 记左右端点分别为a,b, 步数step为b - a + min(startPos - a, b - startPos)
            # 如果step <= k，那么直接加上右端点的值，否则就要减去左端的值
            while queue and queue[0][0] < startPos and \
                    fruits[point][0] - queue[0][0] + min(startPos - queue[0][0], fruits[point][0] - startPos) > k:
                tmp -= queue[0][1]
                queue.popleft()
            tmp += fruits[point][1]
            ans = max(tmp, ans)
            point += 1
        return ans


if __name__ == '__main__':
    fruits = [[0, 9], [4, 1], [5, 7], [6, 2], [7, 4], [10, 9]]
    startPos = 5
    k = 4
    s = Solution()
    print(s.maxTotalFruits(fruits, startPos, k))
