# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 3
@time: 2022/1/16 10:48 上午
@desc: 
"""
from typing import List


class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        # 倒序dp
        n = len(questions)
        dp = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            score, step = questions[i]
            # 间隔step，实际要+1
            if i + step + 1 < len(dp):
                score += dp[i + step + 1]
            dp[i] = max(score, dp[i + 1])
        return dp[0]

    def mostPoints2(self, questions: List[List[int]]) -> int:
        # 正序dp
        n = len(questions)
        dp = [0] * (n + 1)
        for i in range(n):
            score, step = questions[i]
            # 跳过的情况
            dp[i + 1] = max(dp[i], dp[i + 1])
            # 不跳过的情况，如果间隔越界，则给最后一题
            next_step = min(i + step + 1, n)
            dp[next_step] = max(dp[next_step], dp[i] + score)
        return dp[n]


if __name__ == '__main__':
    questions = [[3, 2], [4, 3], [4, 4], [2, 5]]
    s = Solution()
    print(s.mostPoints2(questions))
